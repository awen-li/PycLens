# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: ItimerTest_test_itimer_exc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(signal.ItimerError, signal.setitimer, -1, 0)
    if 0:
        self.assertRaises(signal.ItimerError, signal.setitimer, signal.ITIMER_REAL, -1)
