# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_finalization.py
# case: CycleChainFinalizationTest_test_homogenous

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_non_resurrecting_chain([SimpleChained] * 3)
