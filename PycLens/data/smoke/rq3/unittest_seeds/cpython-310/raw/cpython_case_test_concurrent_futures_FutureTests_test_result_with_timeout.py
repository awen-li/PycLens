# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: FutureTests_test_result_with_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(futures.TimeoutError, PENDING_FUTURE.result, timeout=0)
    self.assertRaises(futures.TimeoutError, RUNNING_FUTURE.result, timeout=0)
    self.assertRaises(futures.CancelledError, CANCELLED_FUTURE.result, timeout=0)
    self.assertRaises(futures.CancelledError, CANCELLED_AND_NOTIFIED_FUTURE.result, timeout=0)
    self.assertRaises(OSError, EXCEPTION_FUTURE.result, timeout=0)
    self.assertEqual(SUCCESSFUL_FUTURE.result(timeout=0), 42)
