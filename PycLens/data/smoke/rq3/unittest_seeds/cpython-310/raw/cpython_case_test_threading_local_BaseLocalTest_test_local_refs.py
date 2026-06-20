# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading_local.py
# case: BaseLocalTest_test_local_refs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._local_refs(20)
    self._local_refs(50)
    self._local_refs(100)
