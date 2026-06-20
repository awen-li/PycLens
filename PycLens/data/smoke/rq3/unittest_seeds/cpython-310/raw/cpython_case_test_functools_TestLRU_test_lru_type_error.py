# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_type_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.lru_cache(maxsize=None)
    def infinite_cache(o):
        pass

    @functools.lru_cache(maxsize=10)
    def limited_cache(o):
        pass
    with self.assertRaises(TypeError):
        infinite_cache([])
    with self.assertRaises(TypeError):
        limited_cache([])
