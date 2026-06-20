# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_sigfpe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_fatal_error('\n            import faulthandler\n            faulthandler.enable()\n            faulthandler._sigfpe()\n            ', 3, 'Floating point exception')
