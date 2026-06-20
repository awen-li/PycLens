# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_weak_destroy_while_iterating

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = [ustr(c) for c in ('a', 'b', 'c')]
    s = WeakSet(items)
    it = iter(s)
    next(it)
    del items[-1]
    gc.collect()
    self.assertIn(len(list(it)), [len(items), len(items) - 1])
    del it
    self.assertEqual(len(s), len(items))
