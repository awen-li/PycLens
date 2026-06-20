# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: WaitTests_test_all_completed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future1 = self.executor.submit(divmod, 2, 0)
    future2 = self.executor.submit(mul, 2, 21)
    (finished, pending) = futures.wait([SUCCESSFUL_FUTURE, CANCELLED_AND_NOTIFIED_FUTURE, EXCEPTION_FUTURE, future1, future2], return_when=futures.ALL_COMPLETED)
    self.assertEqual(set([SUCCESSFUL_FUTURE, CANCELLED_AND_NOTIFIED_FUTURE, EXCEPTION_FUTURE, future1, future2]), finished)
    self.assertEqual(set(), pending)
