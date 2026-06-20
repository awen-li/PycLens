# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestChainMap_test_bool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(ChainMap())
    self.assertFalse(ChainMap({}, {}))
    self.assertTrue(ChainMap({1: 2}, {}))
    self.assertTrue(ChainMap({}, {1: 2}))
