# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCache_test_cache

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @self.module.cache
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)
    self.assertEqual([fib(n) for n in range(16)], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610])
    self.assertEqual(fib.cache_info(), self.module._CacheInfo(hits=28, misses=16, maxsize=None, currsize=16))
    fib.cache_clear()
    self.assertEqual(fib.cache_info(), self.module._CacheInfo(hits=0, misses=0, maxsize=None, currsize=0))
