# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_bug_35780

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    once = True

    @self.module.lru_cache(maxsize=10)
    def f(x):
        nonlocal once
        rv = f'.{x}.'
        if x == 20 and once:
            once = False
            rv = f(x)
        return rv
    for x in range(15):
        self.assertEqual(f(x), f'.{x}.')
    self.assertEqual(f.cache_info().currsize, 10)
    self.assertEqual(f(20), '.20.')
    self.assertEqual(f.cache_info().currsize, 10)
