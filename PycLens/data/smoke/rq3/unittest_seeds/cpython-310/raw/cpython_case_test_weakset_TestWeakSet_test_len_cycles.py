# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_len_cycles

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    N = 20
    items = [RefCycle() for i in range(N)]
    s = WeakSet(items)
    del items
    it = iter(s)
    try:
        next(it)
    except StopIteration:
        pass
    gc.collect()
    n1 = len(s)
    del it
    gc.collect()
    gc.collect()
    n2 = len(s)
    self.assertIn(n1, (0, 1))
    self.assertEqual(n2, 0)
