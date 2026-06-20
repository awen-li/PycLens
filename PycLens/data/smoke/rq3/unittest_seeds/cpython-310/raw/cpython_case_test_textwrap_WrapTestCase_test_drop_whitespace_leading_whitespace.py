# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_drop_whitespace_leading_whitespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = ' This is a sentence with leading whitespace.'
    self.check_wrap(text, 50, [' This is a sentence with leading whitespace.'])
    self.check_wrap(text, 30, [' This is a sentence with', 'leading whitespace.'])
