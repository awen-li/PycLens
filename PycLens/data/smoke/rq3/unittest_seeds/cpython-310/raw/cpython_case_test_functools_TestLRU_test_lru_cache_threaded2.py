# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_cache_threaded2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (n, m) = (5, 7)
    start = threading.Barrier(n + 1)
    pause = threading.Barrier(n + 1)
    stop = threading.Barrier(n + 1)

    @self.module.lru_cache(maxsize=m * n)
    def f(x):
        pause.wait(10)
        return 3 * x
    self.assertEqual(f.cache_info(), (0, 0, m * n, 0))

    def test():
        for i in range(m):
            start.wait(10)
            self.assertEqual(f(i), 3 * i)
            stop.wait(10)
    threads = [threading.Thread(target=test) for k in range(n)]
    with threading_helper.start_threads(threads):
        for i in range(m):
            start.wait(10)
            stop.reset()
            pause.wait(10)
            start.reset()
            stop.wait(10)
            pause.reset()
            self.assertEqual(f.cache_info(), (0, (i + 1) * n, m * n, i + 1))
