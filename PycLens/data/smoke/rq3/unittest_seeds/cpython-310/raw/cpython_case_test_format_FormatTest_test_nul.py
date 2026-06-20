# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_format.py
# case: FormatTest_test_nul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testcommon('a\x00b', (), 'a\x00b')
    testcommon('a%cb', (0,), 'a\x00b')
    testformat('a%sb', ('c\x00d',), 'ac\x00db')
    testcommon(b'a%sb', (b'c\x00d',), b'ac\x00db')
