"""Extract pybcSEC fuzzing seeds from CPython unittest files."""

from __future__ import annotations

import ast
from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
import shutil
import textwrap


SEED_TARGET_NAME = "__pybcsec_seed__"


@dataclass(frozen=True)
class ExtractSeedResult:
    cases: int
    files: int
    skipped: int
    duplicates: int
    out_dir: Path


def extract_cpython_test_seeds(
    cpython_src: Path,
    out_dir: Path,
    limit: int | None = None,
    max_bytes: int | None = None,
    skip_patterns: list[str] | None = None,
    clear: bool = False,
    include_files: bool = False,
    deduplicate: bool = True,
) -> ExtractSeedResult:
    skip_patterns = skip_patterns or []
    test_dir = cpython_src / "Lib" / "test"
    if not test_dir.is_dir():
        raise RuntimeError(f"CPython test directory not found: {test_dir}")

    out_dir.mkdir(parents=True, exist_ok=True)
    if clear:
        for old_seed in out_dir.glob("*.py"):
            old_seed.unlink()

    copied = 0
    skipped = 0
    duplicates = 0
    files_copied = 0
    seen_cases: set[str] = set()
    for source in sorted(test_dir.glob("test_*.py")):
        if limit is not None and copied >= limit:
            break
        if _should_skip(source, max_bytes, skip_patterns):
            skipped += 1
            continue
        text = source.read_text(encoding="utf-8", errors="replace")
        if not _is_syntax_seed(text):
            skipped += 1
            continue

        module = ast.parse(text, filename=str(source))
        cases = _extract_cases(module)
        if not cases:
            skipped += 1
            continue

        for case in cases:
            if limit is not None and copied >= limit:
                break
            rendered = _render_case_seed(source, case)
            try:
                compile(rendered, f"{source}:{case.name}", "exec")
            except SyntaxError:
                skipped += 1
                continue
            digest = _seed_digest(rendered)
            if deduplicate and digest in seen_cases:
                duplicates += 1
                continue
            seen_cases.add(digest)
            dest = _unique_path(out_dir, f"cpython_case_{_safe_stem(source.stem)}_{_safe_stem(case.name)}")
            dest.write_text(rendered, encoding="utf-8")
            copied += 1

        if include_files:
            dest = out_dir / f"cpython_file_{_safe_stem(source.stem)}.py"
            shutil.copyfile(source, dest)
            files_copied += 1

    return ExtractSeedResult(
        cases=copied,
        files=files_copied,
        skipped=skipped,
        duplicates=duplicates,
        out_dir=out_dir,
    )


def _should_skip(path: Path, max_bytes: int | None, skip_patterns: list[str]) -> bool:
    if max_bytes is not None and path.stat().st_size > max_bytes:
        return True
    return any(re.search(pattern, path.stem) for pattern in skip_patterns)


def _is_syntax_seed(text: str) -> bool:
    try:
        ast.parse(text)
    except SyntaxError:
        return False
    return True


def _seed_digest(rendered: str) -> str:
    body = "\n".join(
        line
        for line in rendered.splitlines()
        if not line.startswith("# source:") and not line.startswith("# case:")
    )
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


class CaseSeed:
    def __init__(self, name: str, node: ast.FunctionDef | ast.AsyncFunctionDef, *, method: bool) -> None:
        self.name = name
        self.node = node
        self.method = method


def _extract_cases(module: ast.Module) -> list[CaseSeed]:
    visitor = _CaseVisitor()
    visitor.visit(module)
    return visitor.cases


class _CaseVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.cases: list[CaseSeed] = []
        self._stack: list[str] = []
        self._class_depth = 0

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self._stack.append(node.name)
        self._class_depth += 1
        self.generic_visit(node)
        self._class_depth -= 1
        self._stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._visit_function(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._visit_function(node)

    def _visit_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        if node.name.startswith("test_"):
            qualname = "_".join([*self._stack, node.name]) if self._stack else node.name
            self.cases.append(CaseSeed(qualname, node, method=self._class_depth > 0))
        self._stack.append(node.name)
        self.generic_visit(node)
        self._stack.pop()


def _render_case_seed(source: Path, case: CaseSeed) -> str:
    args = ast.arguments(
        posonlyargs=[],
        args=[],
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[],
    )
    if isinstance(case.node, ast.AsyncFunctionDef):
        func = ast.AsyncFunctionDef(
            name=SEED_TARGET_NAME,
            args=args,
            body=_case_body(case),
            decorator_list=[],
            returns=None,
            type_comment=None,
        )
    else:
        func = ast.FunctionDef(
            name=SEED_TARGET_NAME,
            args=args,
            body=_case_body(case),
            decorator_list=[],
            returns=None,
            type_comment=None,
        )
    ast.fix_missing_locations(func)
    body = ast.unparse(func)
    return (
        f"# pybcsec-seed-target: {SEED_TARGET_NAME}\n"
        f"# source: {source}\n"
        f"# case: {case.name}\n\n"
        f"{body}\n"
    )


def _case_body(case: CaseSeed) -> list[ast.stmt]:
    prelude = "self = __pybcsec_self__ = object()\n"
    if case.method:
        prelude += "__pybcsec_self__ = self\n"
    prelude_body = ast.parse(prelude).body
    body = [stmt for stmt in case.node.body if not isinstance(stmt, ast.Expr) or not _is_docstring(stmt)]
    if not body:
        body = [ast.Pass()]
    return prelude_body + _dedent_nodes(body)


def _dedent_nodes(nodes: list[ast.stmt]) -> list[ast.stmt]:
    text = "\n".join(ast.unparse(node) for node in nodes)
    return ast.parse(textwrap.dedent(text)).body


def _is_docstring(stmt: ast.Expr) -> bool:
    return isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, str)


def _safe_stem(stem: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]+", "_", stem)


def _unique_path(out_dir: Path, stem: str) -> Path:
    path = out_dir / f"{stem}.py"
    if not path.exists():
        return path
    index = 1
    while True:
        path = out_dir / f"{stem}_{index}.py"
        if not path.exists():
            return path
        index += 1
