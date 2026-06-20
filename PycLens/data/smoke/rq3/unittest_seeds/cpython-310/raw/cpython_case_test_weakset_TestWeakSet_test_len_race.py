# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_len_race

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(gc.set_threshold, *gc.get_threshold())
    for th in range(1, 100):
        N = 20
        gc.collect(0)
        gc.set_threshold(th, th, th)
        items = [RefCycle() for i in range(N)]
        s = WeakSet(items)
        del items
        it = iter(s)
        try:
            next(it)
        except StopIteration:
            pass
        n1 = len(s)
        del it
        n2 = len(s)
        self.assertGreaterEqual(n1, 0)
        self.assertLessEqual(n1, N)
        self.assertGreaterEqual(n2, 0)
        self.assertLessEqual(n2, n1)
