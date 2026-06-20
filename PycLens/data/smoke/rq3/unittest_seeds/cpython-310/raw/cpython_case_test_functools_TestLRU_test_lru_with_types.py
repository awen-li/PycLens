# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_with_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for maxsize in (None, 128):

        @self.module.lru_cache(maxsize=maxsize, typed=True)
        def square(x):
            return x * x
        self.assertEqual(square(3), 9)
        self.assertEqual(type(square(3)), type(9))
        self.assertEqual(square(3.0), 9.0)
        self.assertEqual(type(square(3.0)), type(9.0))
        self.assertEqual(square(x=3), 9)
        self.assertEqual(type(square(x=3)), type(9))
        self.assertEqual(square(x=3.0), 9.0)
        self.assertEqual(type(square(x=3.0)), type(9.0))
        self.assertEqual(square.cache_info().hits, 4)
        self.assertEqual(square.cache_info().misses, 4)
