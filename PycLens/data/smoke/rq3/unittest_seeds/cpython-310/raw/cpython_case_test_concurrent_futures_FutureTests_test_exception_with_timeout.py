# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_exception_with_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(futures.TimeoutError, PENDING_FUTURE.exception, timeout=0)
    self.assertRaises(futures.TimeoutError, RUNNING_FUTURE.exception, timeout=0)
    self.assertRaises(futures.CancelledError, CANCELLED_FUTURE.exception, timeout=0)
    self.assertRaises(futures.CancelledError, CANCELLED_AND_NOTIFIED_FUTURE.exception, timeout=0)
    self.assertTrue(isinstance(EXCEPTION_FUTURE.exception(timeout=0), OSError))
    self.assertEqual(SUCCESSFUL_FUTURE.exception(timeout=0), None)
