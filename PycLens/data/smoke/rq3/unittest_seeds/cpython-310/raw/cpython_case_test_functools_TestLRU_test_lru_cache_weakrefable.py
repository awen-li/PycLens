# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_cache_weakrefable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @self.module.lru_cache
    def test_function(x):
        return x

    class A:

        @self.module.lru_cache
        def test_method(self, x):
            return (self, x)

        @staticmethod
        @self.module.lru_cache
        def test_staticmethod(x):
            return (self, x)
    refs = [weakref.ref(test_function), weakref.ref(A.test_method), weakref.ref(A.test_staticmethod)]
    for ref in refs:
        self.assertIsNotNone(ref())
    del A
    del test_function
    gc.collect()
    for ref in refs:
        self.assertIsNone(ref())
