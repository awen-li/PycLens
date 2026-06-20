# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_stderr_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.check_stderr_none():
        faulthandler.enable()
    with self.check_stderr_none():
        faulthandler.dump_traceback()
    with self.check_stderr_none():
        faulthandler.dump_traceback_later(0.001)
    if hasattr(faulthandler, 'register'):
        with self.check_stderr_none():
            faulthandler.register(signal.SIGUSR1)
