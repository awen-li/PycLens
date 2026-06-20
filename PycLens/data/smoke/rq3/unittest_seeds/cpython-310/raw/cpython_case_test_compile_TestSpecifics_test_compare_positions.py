# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_compare_positions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (opname, op) in [('COMPARE_OP', '<'), ('COMPARE_OP', '<='), ('COMPARE_OP', '>'), ('COMPARE_OP', '>='), ('CONTAINS_OP', 'in'), ('CONTAINS_OP', 'not in'), ('IS_OP', 'is'), ('IS_OP', 'is not')]:
        expr = f'a {op} b {op} c'
        expected_lines = 2 * [2]
        for source in [f'\\\n{expr}', f'if \\\n{expr}: x', f'x if \\\n{expr} else y']:
            code = compile(source, '<test>', 'exec')
            all_lines = (line for (start, stop, line) in code.co_lines() for _ in range(start, stop, 2))
            actual_lines = [line for (instruction, line) in zip(dis.get_instructions(code), all_lines, strict=True) if instruction.opname == opname]
            with self.subTest(source):
                self.assertEqual(actual_lines, expected_lines)
