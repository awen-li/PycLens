# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: IndentTestCases_test_initial_indent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expect = ['     This paragraph will be filled,', 'first without any indentation, and then', 'with some (including a hanging indent).']
    result = wrap(self.text, 40, initial_indent='     ')
    self.check(result, expect)
    expect = '\n'.join(expect)
    result = fill(self.text, 40, initial_indent='     ')
    self.check(result, expect)
