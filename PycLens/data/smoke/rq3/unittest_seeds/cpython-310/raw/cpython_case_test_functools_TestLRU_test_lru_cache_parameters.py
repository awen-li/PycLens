# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_cache_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @self.module.lru_cache(maxsize=2)
    def f():
        return 1
    self.assertEqual(f.cache_parameters(), {'maxsize': 2, 'typed': False})

    @self.module.lru_cache(maxsize=1000, typed=True)
    def f():
        return 1
    self.assertEqual(f.cache_parameters(), {'maxsize': 1000, 'typed': True})
