# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_sigill

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_fatal_error('\n            import faulthandler\n            import signal\n\n            faulthandler.enable()\n            signal.raise_signal(signal.SIGILL)\n            ', 5, 'Illegal instruction')
