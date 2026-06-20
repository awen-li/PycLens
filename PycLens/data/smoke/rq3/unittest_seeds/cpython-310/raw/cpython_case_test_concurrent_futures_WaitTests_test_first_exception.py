# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: WaitTests_test_first_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future1 = self.executor.submit(mul, 2, 21)
    future2 = self.executor.submit(sleep_and_raise, 1.5)
    future3 = self.executor.submit(time.sleep, 3)
    (finished, pending) = futures.wait([future1, future2, future3], return_when=futures.FIRST_EXCEPTION)
    self.assertEqual(set([future1, future2]), finished)
    self.assertEqual(set([future3]), pending)
