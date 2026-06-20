# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_running

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(PENDING_FUTURE.running())
    self.assertTrue(RUNNING_FUTURE.running())
    self.assertFalse(CANCELLED_FUTURE.running())
    self.assertFalse(CANCELLED_AND_NOTIFIED_FUTURE.running())
    self.assertFalse(EXCEPTION_FUTURE.running())
    self.assertFalse(SUCCESSFUL_FUTURE.running())
