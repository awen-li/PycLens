# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_cache_decoration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(zomg: 'zomg_annotation'):
        """f doc string"""
        return 42
    g = self.module.lru_cache()(f)
    for attr in self.module.WRAPPER_ASSIGNMENTS:
        self.assertEqual(getattr(g, attr), getattr(f, attr))
