# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_with_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for maxsize in (None, 128):

        @self.module.lru_cache(maxsize)
        def func(i):
            return 'abc'[i]
        self.assertEqual(func(0), 'a')
        with self.assertRaises(IndexError) as cm:
            func(15)
        self.assertIsNone(cm.exception.__context__)
        with self.assertRaises(IndexError):
            func(15)
