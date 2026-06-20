# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_collect_generations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gc.collect()
    x = []
    gc.collect(0)
    (a, b, c) = gc.get_count()
    gc.collect(1)
    (d, e, f) = gc.get_count()
    gc.collect(2)
    (g, h, i) = gc.get_count()
    self.assertEqual((b, c), (1, 0))
    self.assertEqual((e, f), (0, 1))
    self.assertEqual((h, i), (0, 0))
