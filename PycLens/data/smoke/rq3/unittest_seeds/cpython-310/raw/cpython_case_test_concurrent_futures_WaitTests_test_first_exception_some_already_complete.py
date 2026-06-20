# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: WaitTests_test_first_exception_some_already_complete

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future1 = self.executor.submit(divmod, 21, 0)
    future2 = self.executor.submit(time.sleep, 1.5)
    (finished, pending) = futures.wait([SUCCESSFUL_FUTURE, CANCELLED_FUTURE, CANCELLED_AND_NOTIFIED_FUTURE, future1, future2], return_when=futures.FIRST_EXCEPTION)
    self.assertEqual(set([SUCCESSFUL_FUTURE, CANCELLED_AND_NOTIFIED_FUTURE, future1]), finished)
    self.assertEqual(set([CANCELLED_FUTURE, future2]), pending)
