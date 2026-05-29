"""Data collectors for pybcSEC study inputs."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import time
import urllib.error
import urllib.parse
import urllib.request
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Sequence


PYPI_JSON_URL = "https://pypi.org/pypi/{name}/json"
PYPI_DISTRIBUTIONS = ("wheel", "sdist")
DOWNLOAD_FIELDNAMES = [
    "package",
    "version",
    "filename",
    "packagetype",
    "python_version",
    "url",
    "size",
    "sha256",
    "local_path",
    "status",
    "error",
]


@dataclass(frozen=True)
class CollectionConfig:
    data_dir: Path
    out_dir: Path | None
    csv_out: Path | None
    json_out: Path | None
    include: Sequence[str]
    max_files_per_kind: int
    timeout: int
    delay: float
    force: bool
    quiet: bool
    max_age_years: int | None
    workers: int


@dataclass
class DownloadRecord:
    package: str
    version: str
    filename: str
    packagetype: str
    python_version: str
    url: str
    size: int
    sha256: str
    local_path: str
    status: str
    error: str = ""


class DataCollector(ABC):
    source_name: str

    def __init__(self, config: CollectionConfig) -> None:
        self.config = config

    @abstractmethod
    def collect(self, packages: Sequence[str]) -> list[DownloadRecord]:
        """Collect source data for the supplied package names."""

    @abstractmethod
    def default_artifact_dir(self) -> Path:
        """Return the default artifact directory for this source."""

    @abstractmethod
    def default_manifest_path(self) -> Path:
        """Return the default CSV manifest path for this source."""

    def artifact_dir(self) -> Path:
        return self.config.out_dir or self.default_artifact_dir()

    def manifest_path(self) -> Path:
        return self.config.csv_out or self.default_manifest_path()

    def progress(self, message: str) -> None:
        if not self.config.quiet:
            print(message)

    def write_outputs(self, records: Sequence[DownloadRecord]) -> Path:
        csv_out = self.manifest_path()
        csv_out.parent.mkdir(parents=True, exist_ok=True)
        with csv_out.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=DOWNLOAD_FIELDNAMES)
            writer.writeheader()
            writer.writerows(asdict(record) for record in records)

        if self.config.json_out:
            self.config.json_out.parent.mkdir(parents=True, exist_ok=True)
            manifest = {
                "component": "data_collection",
                "source": self.source_name,
                "records": [asdict(record) for record in records],
            }
            self.config.json_out.write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )

        return csv_out


class PyPICollector(DataCollector):
    source_name = "pypi"

    def default_artifact_dir(self) -> Path:
        return self.config.data_dir / "artifacts" / self.source_name

    def default_manifest_path(self) -> Path:
        return self.config.data_dir / "sources" / self.source_name / "manifest.csv"

    def collect(self, packages: Sequence[str]) -> list[DownloadRecord]:
        out_dir = self.artifact_dir()
        include = tuple(self.config.include or PYPI_DISTRIBUTIONS)
        cutoff = upload_cutoff(self.config.max_age_years)
        workers = max(1, self.config.workers)
        existing_records = [] if self.config.force else read_download_records(self.manifest_path())
        completed_packages = completed_package_names(existing_records)
        pending_packages = [package for package in packages if package not in completed_packages]
        records: list[DownloadRecord] = list(existing_records)

        self.progress(
            "collecting PyPI artifacts: packages={packages}, pending={pending}, skipped={skipped}, include={include}, max_age_years={age}, workers={workers}, output={out}".format(
                packages=len(packages),
                pending=len(pending_packages),
                skipped=len(packages) - len(pending_packages),
                include=",".join(include),
                age=self.config.max_age_years if self.config.max_age_years is not None else "all",
                workers=workers,
                out=out_dir,
            )
        )

        if not pending_packages:
            return records

        if workers == 1:
            for package_index, package in enumerate(pending_packages, start=1):
                package_records = self.collect_package(package, package_index, len(pending_packages), out_dir, include, cutoff)
                append_download_records(self.manifest_path(), package_records)
                records.extend(package_records)
            return records

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {
                executor.submit(
                    self.collect_package,
                    package,
                    package_index,
                    len(pending_packages),
                    out_dir,
                    include,
                    cutoff,
                ): package
                for package_index, package in enumerate(pending_packages, start=1)
            }
            for future in as_completed(futures):
                package_records = future.result()
                append_download_records(self.manifest_path(), package_records)
                records.extend(package_records)

        return records

    def collect_package(
        self,
        package: str,
        package_index: int,
        package_count: int,
        out_dir: Path,
        include: Sequence[str],
        cutoff: datetime | None,
    ) -> list[DownloadRecord]:
        records: list[DownloadRecord] = []
        package_key = urllib.parse.quote(package)
        metadata_url = PYPI_JSON_URL.format(name=package_key)
        self.progress(f"[{package_index}/{package_count}] metadata {package}")
        try:
            project = fetch_json(metadata_url, self.config.timeout)
            version = project["info"]["version"]
            release_files = select_release_files(
                project,
                include,
                self.config.max_files_per_kind,
                cutoff,
            )
            if not release_files:
                self.progress(
                    f"[{package_index}/{package_count}] no recent matching release files for {package} {version}"
                )
                return [
                    DownloadRecord(
                        package=package,
                        version=version,
                        filename="",
                        packagetype="",
                        python_version="",
                        url=metadata_url,
                        size=0,
                        sha256="",
                        local_path="",
                        status="no_recent_release_files",
                    )
                ]

            for file_index, file_info in enumerate(release_files, start=1):
                filename = file_info["filename"]
                dest = out_dir / package / version / filename
                expected_sha256 = file_info.get("digests", {}).get("sha256", "")
                expected_size = int(file_info.get("size", 0))
                if dest.exists() and not self.config.force and file_is_complete(dest, expected_sha256, expected_size):
                    status = "exists"
                else:
                    self.progress(
                        f"[{package_index}/{package_count}] download {file_index}/{len(release_files)} {filename}"
                    )
                    download_file(file_info["url"], dest, self.config.timeout, expected_size)
                    status = "downloaded" if not dest.exists() else "downloaded"

                actual_sha256 = sha256_file(dest)
                if expected_sha256 and actual_sha256 != expected_sha256:
                    status = "sha256_mismatch"

                records.append(
                    DownloadRecord(
                        package=package,
                        version=version,
                        filename=filename,
                        packagetype=file_info.get("packagetype", ""),
                        python_version=file_info.get("python_version", ""),
                        url=file_info["url"],
                        size=int(file_info.get("size", 0)),
                        sha256=actual_sha256,
                        local_path=str(dest),
                        status=status,
                    )
                )
                self.progress(
                    f"[{package_index}/{package_count}] {status} {filename} sha256={actual_sha256[:12]}"
                )
                time.sleep(self.config.delay)
        except (OSError, urllib.error.URLError, KeyError, json.JSONDecodeError) as exc:
            self.progress(f"[{package_index}/{package_count}] error {package}: {type(exc).__name__}: {exc}")
            records.append(
                DownloadRecord(
                    package=package,
                    version="",
                    filename="",
                    packagetype="",
                    python_version="",
                    url=metadata_url,
                    size=0,
                    sha256="",
                    local_path="",
                    status="error",
                    error=f"{type(exc).__name__}: {exc}",
                )
            )
        return records


class SuspiciousPyPICollector(PyPICollector):
    source_name = "suspicious_pypi"


class LocalArtifactCollector(DataCollector):
    source_name = "local"

    def default_artifact_dir(self) -> Path:
        return self.config.data_dir / "artifacts" / self.source_name

    def default_manifest_path(self) -> Path:
        return self.config.data_dir / "sources" / self.source_name / "manifest.csv"

    def collect(self, paths: Sequence[str]) -> list[DownloadRecord]:
        out_dir = self.artifact_dir()
        records: list[DownloadRecord] = []
        self.progress(f"collecting local artifacts: inputs={len(paths)}, output={out_dir}")

        for index, raw_path in enumerate(paths, start=1):
            src = Path(raw_path)
            name = src.name or f"artifact-{index}"
            dest = unique_destination(out_dir / name)
            try:
                if not src.exists():
                    raise FileNotFoundError(src)
                if dest.exists() and not self.config.force:
                    status = "exists"
                elif src.is_dir():
                    if dest.exists():
                        shutil.rmtree(dest)
                    shutil.copytree(src, dest)
                    status = "copied"
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dest)
                    status = "copied"

                digest = sha256_tree(dest) if dest.is_dir() else sha256_file(dest)
                size = path_size(dest)
                self.progress(f"[{index}/{len(paths)}] {status} {src} -> {dest}")
                records.append(
                    DownloadRecord(
                        package=src.stem,
                        version="",
                        filename=name,
                        packagetype="directory" if dest.is_dir() else "file",
                        python_version="",
                        url=str(src),
                        size=size,
                        sha256=digest,
                        local_path=str(dest),
                        status=status,
                    )
                )
            except OSError as exc:
                self.progress(f"[{index}/{len(paths)}] error {src}: {type(exc).__name__}: {exc}")
                records.append(
                    DownloadRecord(
                        package=src.stem,
                        version="",
                        filename=name,
                        packagetype="",
                        python_version="",
                        url=str(src),
                        size=0,
                        sha256="",
                        local_path="",
                        status="error",
                        error=f"{type(exc).__name__}: {exc}",
                    )
                )

        return records


class GitHubReleaseCollector(DataCollector):
    source_name = "github_releases"

    def default_artifact_dir(self) -> Path:
        return self.config.data_dir / "artifacts" / self.source_name

    def default_manifest_path(self) -> Path:
        return self.config.data_dir / "sources" / self.source_name / "manifest.csv"

    def collect(self, repos: Sequence[str]) -> list[DownloadRecord]:
        out_dir = self.artifact_dir()
        records: list[DownloadRecord] = []
        self.progress(f"collecting GitHub release assets: repos={len(repos)}, output={out_dir}")

        for repo_index, repo in enumerate(repos, start=1):
            api_url = f"https://api.github.com/repos/{repo}/releases/latest"
            self.progress(f"[{repo_index}/{len(repos)}] metadata {repo}")
            try:
                release = fetch_json(api_url, self.config.timeout)
                tag = release.get("tag_name", "")
                assets = select_github_assets(release, self.config.include, self.config.max_files_per_kind)
                if not assets:
                    self.progress(f"[{repo_index}/{len(repos)}] no matching release assets for {repo} {tag}")
                    records.append(
                        DownloadRecord(
                            package=repo,
                            version=tag,
                            filename="",
                            packagetype="github_release",
                            python_version="",
                            url=api_url,
                            size=0,
                            sha256="",
                            local_path="",
                            status="no_release_assets",
                        )
                    )
                    continue

                owner_repo = repo.replace("/", "__")
                for asset_index, asset in enumerate(assets, start=1):
                    filename = asset["name"]
                    dest = out_dir / owner_repo / tag / filename
                    expected_size = int(asset.get("size", 0))
                    if dest.exists() and not self.config.force and file_is_complete(dest, "", expected_size):
                        status = "exists"
                    else:
                        self.progress(
                            f"[{repo_index}/{len(repos)}] download {asset_index}/{len(assets)} {filename}"
                        )
                        download_file(asset["browser_download_url"], dest, self.config.timeout, expected_size)
                        status = "downloaded"
                    digest = sha256_file(dest)
                    records.append(
                        DownloadRecord(
                            package=repo,
                            version=tag,
                            filename=filename,
                            packagetype=artifact_kind(Path(filename)),
                            python_version="",
                            url=asset["browser_download_url"],
                            size=int(asset.get("size", 0)),
                            sha256=digest,
                            local_path=str(dest),
                            status=status,
                        )
                    )
                    self.progress(f"[{repo_index}/{len(repos)}] {status} {filename} sha256={digest[:12]}")
                    time.sleep(self.config.delay)
            except (OSError, urllib.error.URLError, KeyError, json.JSONDecodeError) as exc:
                self.progress(f"[{repo_index}/{len(repos)}] error {repo}: {type(exc).__name__}: {exc}")
                records.append(
                    DownloadRecord(
                        package=repo,
                        version="",
                        filename="",
                        packagetype="github_release",
                        python_version="",
                        url=api_url,
                        size=0,
                        sha256="",
                        local_path="",
                        status="error",
                        error=f"{type(exc).__name__}: {exc}",
                    )
                )

        return records


def fetch_json(url: str, timeout: int) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "pybcSEC-study-tool/0.1"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def read_download_records(path: Path) -> list[DownloadRecord]:
    if not path.exists():
        return []
    records: list[DownloadRecord] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            records.append(
                DownloadRecord(
                    package=row.get("package", ""),
                    version=row.get("version", ""),
                    filename=row.get("filename", ""),
                    packagetype=row.get("packagetype", ""),
                    python_version=row.get("python_version", ""),
                    url=row.get("url", ""),
                    size=int(row.get("size") or 0),
                    sha256=row.get("sha256", ""),
                    local_path=row.get("local_path", ""),
                    status=row.get("status", ""),
                    error=row.get("error", ""),
                )
            )
    return records


def append_download_records(path: Path, records: Sequence[DownloadRecord]) -> None:
    if not records:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=DOWNLOAD_FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerows(asdict(record) for record in records)


def completed_package_names(records: Sequence[DownloadRecord]) -> set[str]:
    return {
        record.package
        for record in records
        if record.package and record.status not in {"error", "sha256_mismatch"}
    }


def distribution_kind(file_info: dict) -> str:
    packagetype = file_info.get("packagetype", "")
    if packagetype == "bdist_wheel":
        return "wheel"
    if packagetype == "sdist":
        return "sdist"
    return "other"


def select_release_files(
    project: dict,
    include: Sequence[str],
    max_files_per_kind: int,
    cutoff: datetime | None,
) -> list[dict]:
    version = project["info"]["version"]
    files = list(project["releases"].get(version, []))
    selected: list[dict] = []

    for kind in include:
        kind_files = [
            item
            for item in files
            if distribution_kind(item) == kind and is_recent_upload(item, cutoff)
        ]
        kind_files.sort(key=lambda item: item.get("filename", ""))
        selected.extend(kind_files[:max_files_per_kind])

    return selected


def upload_cutoff(max_age_years: int | None) -> datetime | None:
    if max_age_years is None:
        return None
    if max_age_years < 1:
        raise ValueError("max_age_years must be positive")
    return datetime.now(timezone.utc) - timedelta(days=365 * max_age_years)


def is_recent_upload(file_info: dict, cutoff: datetime | None) -> bool:
    if cutoff is None:
        return True
    uploaded_at = parse_upload_time(file_info)
    return uploaded_at is not None and uploaded_at >= cutoff


def parse_upload_time(file_info: dict) -> datetime | None:
    raw = file_info.get("upload_time_iso_8601") or file_info.get("upload_time")
    if not raw:
        return None
    value = str(raw).replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def select_github_assets(release: dict, include: Sequence[str], max_files_per_kind: int) -> list[dict]:
    assets = list(release.get("assets", []))
    if not include:
        selected = assets[:max_files_per_kind]
    else:
        selected = [
            asset
            for asset in assets
            if artifact_kind(Path(asset.get("name", ""))) in include
        ][:max_files_per_kind]
    return [asset for asset in selected if asset.get("browser_download_url")]


def artifact_kind(path: Path) -> str:
    suffixes = "".join(path.suffixes).lower()
    if suffixes.endswith(".whl"):
        return "wheel"
    if suffixes.endswith(".zip"):
        return "zip"
    if suffixes.endswith((".tar.gz", ".tgz", ".tar", ".tar.bz2", ".tbz2", ".tar.xz", ".txz")):
        return "archive"
    if suffixes.endswith(".pyc"):
        return "pyc"
    if suffixes.endswith(".py"):
        return "source"
    return "other"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_is_complete(path: Path, expected_sha256: str, expected_size: int) -> bool:
    try:
        if expected_size and path.stat().st_size != expected_size:
            return False
        if expected_sha256 and sha256_file(path) != expected_sha256:
            return False
        return True
    except OSError:
        return False


def sha256_tree(path: Path) -> str:
    digest = hashlib.sha256()
    for child in sorted(item for item in path.rglob("*") if item.is_file()):
        digest.update(str(child.relative_to(path)).encode("utf-8"))
        digest.update(b"\0")
        with child.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    return digest.hexdigest()


def path_size(path: Path) -> int:
    if path.is_file():
        return path.stat().st_size
    return sum(child.stat().st_size for child in path.rglob("*") if child.is_file())


def unique_destination(path: Path) -> Path:
    if not path.exists():
        return path
    parent = path.parent
    stem = path.stem
    suffix = "".join(path.suffixes)
    for index in range(1, 10000):
        candidate = parent / f"{stem}-{index}{suffix}"
        if not candidate.exists():
            return candidate
    raise FileExistsError(f"too many duplicate artifact names for {path}")


def download_file(url: str, dest: Path, timeout: int, expected_size: int = 0) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.with_name(dest.name + ".part")
    resume_at = part.stat().st_size if part.exists() else 0
    headers = {"User-Agent": "pybcSEC-study-tool/0.1"}
    if resume_at:
        headers["Range"] = f"bytes={resume_at}-"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        mode = "ab" if resume_at and getattr(response, "status", None) == 206 else "wb"
        with part.open(mode) as handle:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                handle.write(chunk)
    if expected_size and part.stat().st_size != expected_size:
        raise OSError(f"incomplete download for {dest}: expected {expected_size}, got {part.stat().st_size}")
    os.replace(part, dest)
