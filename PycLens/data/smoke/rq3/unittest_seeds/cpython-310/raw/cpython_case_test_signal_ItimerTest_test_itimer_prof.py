# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: ItimerTest_test_itimer_prof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.itimer = signal.ITIMER_PROF
    signal.signal(signal.SIGPROF, self.sig_prof)
    signal.setitimer(self.itimer, 0.2, 0.2)
    start_time = time.monotonic()
    while time.monotonic() - start_time < 60.0:
        _ = pow(12345, 67890, 10000019)
        if signal.getitimer(self.itimer) == (0.0, 0.0):
            break
    else:
        self.skipTest('timeout: likely cause: machine too slow or load too high')
    self.assertEqual(signal.getitimer(self.itimer), (0.0, 0.0))
    self.assertEqual(self.hndl_called, True)
