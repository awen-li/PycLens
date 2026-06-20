# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_clinic.py
# case: ClinicParserTest_test_function_not_at_column_0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    function = self.parse_function('\n  module foo\n  foo.bar\n    x: int\n      Nested docstring here, goeth.\n    *\n    y: str\n  Not at column 0!\n')
    self.assertEqual('\nbar($module, /, x, *, y)\n--\n\nNot at column 0!\n\n  x\n    Nested docstring here, goeth.\n'.strip(), function.docstring)
