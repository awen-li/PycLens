# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_no_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @self.module.lru_cache
    def square(x):
        return x ** 2
    self.assertEqual(list(map(square, [10, 20, 10])), [100, 400, 100])
    self.assertEqual(square.cache_info().hits, 1)
    self.assertEqual(square.cache_info().misses, 2)
    self.assertEqual(square.cache_info().maxsize, 128)
    self.assertEqual(square.cache_info().currsize, 2)
