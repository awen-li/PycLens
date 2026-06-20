# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_cache_threaded3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @self.module.lru_cache(maxsize=2)
    def f(x):
        time.sleep(0.01)
        return 3 * x

    def test(i, x):
        with self.subTest(thread=i):
            self.assertEqual(f(x), 3 * x, i)
    threads = [threading.Thread(target=test, args=(i, v)) for (i, v) in enumerate([1, 2, 2, 3, 2])]
    with threading_helper.start_threads(threads):
        pass
