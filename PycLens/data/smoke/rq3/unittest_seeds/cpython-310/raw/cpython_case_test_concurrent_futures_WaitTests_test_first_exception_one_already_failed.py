# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: WaitTests_test_first_exception_one_already_failed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future1 = self.executor.submit(time.sleep, 2)
    (finished, pending) = futures.wait([EXCEPTION_FUTURE, future1], return_when=futures.FIRST_EXCEPTION)
    self.assertEqual(set([EXCEPTION_FUTURE]), finished)
    self.assertEqual(set([future1]), pending)
