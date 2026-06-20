# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_kwargs_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @self.module.lru_cache(maxsize=10)
    def f(**kwargs):
        return list(kwargs.items())
    self.assertEqual(f(a=1, b=2), [('a', 1), ('b', 2)])
    self.assertEqual(f(b=2, a=1), [('b', 2), ('a', 1)])
    self.assertEqual(f.cache_info(), self.module._CacheInfo(hits=0, misses=2, maxsize=10, currsize=2))
