# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def orig(x, y):
        return 3 * x + y
    f = self.module.lru_cache(maxsize=20)(orig)
    (hits, misses, maxsize, currsize) = f.cache_info()
    self.assertEqual(maxsize, 20)
    self.assertEqual(currsize, 0)
    self.assertEqual(hits, 0)
    self.assertEqual(misses, 0)
    domain = range(5)
    for i in range(1000):
        (x, y) = (choice(domain), choice(domain))
        actual = f(x, y)
        expected = orig(x, y)
        self.assertEqual(actual, expected)
    (hits, misses, maxsize, currsize) = f.cache_info()
    self.assertTrue(hits > misses)
    self.assertEqual(hits + misses, 1000)
    self.assertEqual(currsize, 20)
    f.cache_clear()
    (hits, misses, maxsize, currsize) = f.cache_info()
    self.assertEqual(hits, 0)
    self.assertEqual(misses, 0)
    self.assertEqual(currsize, 0)
    f(x, y)
    (hits, misses, maxsize, currsize) = f.cache_info()
    self.assertEqual(hits, 0)
    self.assertEqual(misses, 1)
    self.assertEqual(currsize, 1)
    self.assertIs(f.__wrapped__, orig)
    f.__wrapped__(x, y)
    (hits, misses, maxsize, currsize) = f.cache_info()
    self.assertEqual(hits, 0)
    self.assertEqual(misses, 1)
    self.assertEqual(currsize, 1)

    @self.module.lru_cache(0)
    def f():
        nonlocal f_cnt
        f_cnt += 1
        return 20
    self.assertEqual(f.cache_info().maxsize, 0)
    f_cnt = 0
    for i in range(5):
        self.assertEqual(f(), 20)
    self.assertEqual(f_cnt, 5)
    (hits, misses, maxsize, currsize) = f.cache_info()
    self.assertEqual(hits, 0)
    self.assertEqual(misses, 5)
    self.assertEqual(currsize, 0)

    @self.module.lru_cache(1)
    def f():
        nonlocal f_cnt
        f_cnt += 1
        return 20
    self.assertEqual(f.cache_info().maxsize, 1)
    f_cnt = 0
    for i in range(5):
        self.assertEqual(f(), 20)
    self.assertEqual(f_cnt, 1)
    (hits, misses, maxsize, currsize) = f.cache_info()
    self.assertEqual(hits, 4)
    self.assertEqual(misses, 1)
    self.assertEqual(currsize, 1)

    @self.module.lru_cache(2)
    def f(x):
        nonlocal f_cnt
        f_cnt += 1
        return x * 10
    self.assertEqual(f.cache_info().maxsize, 2)
    f_cnt = 0
    for x in (7, 9, 7, 9, 7, 9, 8, 8, 8, 9, 9, 9, 8, 8, 8, 7):
        self.assertEqual(f(x), x * 10)
    self.assertEqual(f_cnt, 4)
    (hits, misses, maxsize, currsize) = f.cache_info()
    self.assertEqual(hits, 12)
    self.assertEqual(misses, 4)
    self.assertEqual(currsize, 2)
