# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_fatal_error_c_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_fatal_error('\n            import faulthandler\n            faulthandler.enable()\n            faulthandler._fatal_error_c_thread()\n            ', 3, 'in new thread', know_current_thread=False, func='faulthandler_fatal_error_thread', py_fatal_error=True)
