# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_join_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    size = int(sys.maxsize ** 0.5) + 1
    seq = ('A' * size,) * size
    self.assertRaises(OverflowError, ''.join, seq)
