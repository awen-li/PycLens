# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: CosmeticTestCase_test_slices

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_src_roundtrip('a[1]')
    self.check_src_roundtrip('a[1, 2]')
    self.check_src_roundtrip('a[(1, *a)]')
