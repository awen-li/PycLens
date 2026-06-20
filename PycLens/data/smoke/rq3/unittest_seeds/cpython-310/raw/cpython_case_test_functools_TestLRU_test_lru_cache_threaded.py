# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_cache_threaded

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (n, m) = (5, 11)

    def orig(x, y):
        return 3 * x + y
    f = self.module.lru_cache(maxsize=n * m)(orig)
    (hits, misses, maxsize, currsize) = f.cache_info()
    self.assertEqual(currsize, 0)
    start = threading.Event()

    def full(k):
        start.wait(10)
        for _ in range(m):
            self.assertEqual(f(k, 0), orig(k, 0))

    def clear():
        start.wait(10)
        for _ in range(2 * m):
            f.cache_clear()
    orig_si = sys.getswitchinterval()
    support.setswitchinterval(1e-06)
    try:
        threads = [threading.Thread(target=full, args=[k]) for k in range(n)]
        with threading_helper.start_threads(threads):
            start.set()
        (hits, misses, maxsize, currsize) = f.cache_info()
        if self.module is py_functools:
            self.assertLessEqual(misses, n)
            self.assertLessEqual(hits, m * n - misses)
        else:
            self.assertEqual(misses, n)
            self.assertEqual(hits, m * n - misses)
        self.assertEqual(currsize, n)
        threads = [threading.Thread(target=clear)]
        threads += [threading.Thread(target=full, args=[k]) for k in range(n)]
        start.clear()
        with threading_helper.start_threads(threads):
            start.set()
    finally:
        sys.setswitchinterval(orig_si)
