# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: WaitTests_test_first_completed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future1 = self.executor.submit(mul, 21, 2)
    future2 = self.executor.submit(time.sleep, 1.5)
    (done, not_done) = futures.wait([CANCELLED_FUTURE, future1, future2], return_when=futures.FIRST_COMPLETED)
    self.assertEqual(set([future1]), done)
    self.assertEqual(set([CANCELLED_FUTURE, future2]), not_done)
