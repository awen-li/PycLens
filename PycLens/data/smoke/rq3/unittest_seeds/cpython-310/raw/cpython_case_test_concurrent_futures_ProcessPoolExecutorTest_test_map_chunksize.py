# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ProcessPoolExecutorTest_test_map_chunksize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def bad_map():
        list(self.executor.map(pow, range(40), range(40), chunksize=-1))
    ref = list(map(pow, range(40), range(40)))
    self.assertEqual(list(self.executor.map(pow, range(40), range(40), chunksize=6)), ref)
    self.assertEqual(list(self.executor.map(pow, range(40), range(40), chunksize=50)), ref)
    self.assertEqual(list(self.executor.map(pow, range(40), range(40), chunksize=40)), ref)
    self.assertRaises(ValueError, bad_map)
