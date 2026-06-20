# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_lineno_after_no_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def no_code1():
        """doc string"""

    def no_code2():
        a: int
    for func in (no_code1, no_code2):
        with self.subTest(func=func):
            code = func.__code__
            lines = list(code.co_lines())
            self.assertEqual(len(lines), 1)
            (start, end, line) = lines[0]
            self.assertEqual(start, 0)
            self.assertEqual(end, len(code.co_code))
            self.assertEqual(line, code.co_firstlineno)
