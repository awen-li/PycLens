# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorTest_test_map

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(self.executor.map(pow, range(10), range(10))), list(map(pow, range(10), range(10))))
    self.assertEqual(list(self.executor.map(pow, range(10), range(10), chunksize=3)), list(map(pow, range(10), range(10))))
