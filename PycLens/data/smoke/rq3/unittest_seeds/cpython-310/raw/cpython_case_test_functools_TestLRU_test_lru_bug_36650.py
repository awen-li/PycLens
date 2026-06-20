# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_bug_36650

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @self.module.lru_cache()
    def f(x):
        pass
    f(0)
    f(0, **{})
    self.assertEqual(f.cache_info().hits, 1)
