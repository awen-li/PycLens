# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: AsCompletedTests_test_zero_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future1 = self.executor.submit(time.sleep, 2)
    completed_futures = set()
    try:
        for future in futures.as_completed([CANCELLED_AND_NOTIFIED_FUTURE, EXCEPTION_FUTURE, SUCCESSFUL_FUTURE, future1], timeout=0):
            completed_futures.add(future)
    except futures.TimeoutError:
        pass
    self.assertEqual(set([CANCELLED_AND_NOTIFIED_FUTURE, EXCEPTION_FUTURE, SUCCESSFUL_FUTURE]), completed_futures)
