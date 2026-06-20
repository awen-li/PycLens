# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: WaitTests_test_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future1 = self.executor.submit(mul, 6, 7)
    future2 = self.executor.submit(time.sleep, 6)
    (finished, pending) = futures.wait([CANCELLED_AND_NOTIFIED_FUTURE, EXCEPTION_FUTURE, SUCCESSFUL_FUTURE, future1, future2], timeout=5, return_when=futures.ALL_COMPLETED)
    self.assertEqual(set([CANCELLED_AND_NOTIFIED_FUTURE, EXCEPTION_FUTURE, SUCCESSFUL_FUTURE, future1]), finished)
    self.assertEqual(set([future2]), pending)
