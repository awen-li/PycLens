# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WakeupFDTests_test_invalid_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        signal.set_wakeup_fd(signum=signal.SIGINT)
    with self.assertRaises(TypeError):
        signal.set_wakeup_fd(signal.SIGINT, False)
