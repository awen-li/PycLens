# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(int):
        f_cnt = 0

        @self.module.lru_cache(2)
        def f(self, x):
            self.f_cnt += 1
            return x * 10 + self
    a = X(5)
    b = X(5)
    c = X(7)
    self.assertEqual(X.f.cache_info(), (0, 0, 2, 0))
    for x in (1, 2, 2, 3, 1, 1, 1, 2, 3, 3):
        self.assertEqual(a.f(x), x * 10 + 5)
    self.assertEqual((a.f_cnt, b.f_cnt, c.f_cnt), (6, 0, 0))
    self.assertEqual(X.f.cache_info(), (4, 6, 2, 2))
    for x in (1, 2, 1, 1, 1, 1, 3, 2, 2, 2):
        self.assertEqual(b.f(x), x * 10 + 5)
    self.assertEqual((a.f_cnt, b.f_cnt, c.f_cnt), (6, 4, 0))
    self.assertEqual(X.f.cache_info(), (10, 10, 2, 2))
    for x in (2, 1, 1, 1, 1, 2, 1, 3, 2, 1):
        self.assertEqual(c.f(x), x * 10 + 7)
    self.assertEqual((a.f_cnt, b.f_cnt, c.f_cnt), (6, 4, 5))
    self.assertEqual(X.f.cache_info(), (15, 15, 2, 2))
    self.assertEqual(a.f.cache_info(), X.f.cache_info())
    self.assertEqual(b.f.cache_info(), X.f.cache_info())
    self.assertEqual(c.f.cache_info(), X.f.cache_info())
