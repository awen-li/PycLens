# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_drop_whitespace_whitespace_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'abcd    efgh'
    self.check_wrap(text, 6, ['abcd', '    ', 'efgh'], drop_whitespace=False)
    self.check_wrap(text, 6, ['abcd', 'efgh'])
