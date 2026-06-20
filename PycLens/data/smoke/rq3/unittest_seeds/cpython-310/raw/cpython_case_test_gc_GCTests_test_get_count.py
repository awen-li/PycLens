# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_get_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gc.collect()
    (a, b, c) = gc.get_count()
    x = []
    (d, e, f) = gc.get_count()
    self.assertEqual((b, c), (0, 0))
    self.assertEqual((e, f), (0, 0))
    self.assertLess(a, 5)
    self.assertGreater(d, a)
