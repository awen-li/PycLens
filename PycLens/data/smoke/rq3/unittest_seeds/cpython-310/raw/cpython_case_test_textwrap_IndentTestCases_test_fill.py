# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: IndentTestCases_test_fill

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expect = 'This paragraph will be filled, first\nwithout any indentation, and then with\nsome (including a hanging indent).'
    result = fill(self.text, 40)
    self.check(result, expect)
