# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xxlimited.py
# case: TestXXLimited35_test_null

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    null1 = self.module.Null()
    null2 = self.module.Null()
    self.assertNotEqual(null1, null2)
