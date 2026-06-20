# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_with_maxsize_negative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @self.module.lru_cache(maxsize=-10)
    def eq(n):
        return n
    for i in (0, 1):
        self.assertEqual([eq(n) for n in range(150)], list(range(150)))
    self.assertEqual(eq.cache_info(), self.module._CacheInfo(hits=0, misses=300, maxsize=0, currsize=0))
