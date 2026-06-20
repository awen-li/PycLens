# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: SiginterruptTest_test_siginterrupt_off

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interrupted = self.readpipe_interrupted(False)
    self.assertFalse(interrupted)
