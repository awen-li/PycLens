# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: AsCompletedTests_test_no_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future1 = self.executor.submit(mul, 2, 21)
    future2 = self.executor.submit(mul, 7, 6)
    completed = set(futures.as_completed([CANCELLED_AND_NOTIFIED_FUTURE, EXCEPTION_FUTURE, SUCCESSFUL_FUTURE, future1, future2]))
    self.assertEqual(set([CANCELLED_AND_NOTIFIED_FUTURE, EXCEPTION_FUTURE, SUCCESSFUL_FUTURE, future1, future2]), completed)
