# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_done

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(PENDING_FUTURE.done())
    self.assertFalse(RUNNING_FUTURE.done())
    self.assertTrue(CANCELLED_FUTURE.done())
    self.assertTrue(CANCELLED_AND_NOTIFIED_FUTURE.done())
    self.assertTrue(EXCEPTION_FUTURE.done())
    self.assertTrue(SUCCESSFUL_FUTURE.done())
