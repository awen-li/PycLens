# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: ItimerTest_test_itimer_real

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.itimer = signal.ITIMER_REAL
    signal.setitimer(self.itimer, 1.0)
    signal.pause()
    self.assertEqual(self.hndl_called, True)
