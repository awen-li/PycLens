# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: IndentTestCases_test_subsequent_indent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expect = '  * This paragraph will be filled, first\n    without any indentation, and then\n    with some (including a hanging\n    indent).'
    result = fill(self.text, 40, initial_indent='  * ', subsequent_indent='    ')
    self.check(result, expect)
