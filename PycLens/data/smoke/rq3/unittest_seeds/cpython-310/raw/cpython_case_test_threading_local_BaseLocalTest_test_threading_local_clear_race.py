# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading_local.py
# case: BaseLocalTest_test_threading_local_clear_race

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _testcapi = import_module('_testcapi')
    _testcapi.call_in_temporary_c_thread(lambda : None, False)
    for _ in range(1000):
        _ = threading.local()
    _testcapi.join_temporary_c_thread()
