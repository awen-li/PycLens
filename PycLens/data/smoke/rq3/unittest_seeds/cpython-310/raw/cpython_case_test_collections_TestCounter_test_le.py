# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_le

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(Counter(a=3, b=2, c=0) <= Counter('ababa'))
    self.assertFalse(Counter(a=3, b=2) <= Counter('babab'))
