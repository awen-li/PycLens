# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: WaitTests_test_20369

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    future = self.executor.submit(time.sleep, 1.5)
    (done, not_done) = futures.wait([future, future], return_when=futures.ALL_COMPLETED)
    self.assertEqual({future}, done)
    self.assertEqual(set(), not_done)
