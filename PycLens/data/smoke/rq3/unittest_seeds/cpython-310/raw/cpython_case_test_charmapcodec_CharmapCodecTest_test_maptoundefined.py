# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_charmapcodec.py
# case: CharmapCodecTest_test_maptoundefined

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(UnicodeError, str, b'abc\x01', codecname)
