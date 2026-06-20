# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: FinalizationTest_test_refcycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_garbage = gc.garbage[:]
    finalized = False

    def gen():
        nonlocal finalized
        try:
            g = (yield)
            yield 1
        finally:
            finalized = True
    g = gen()
    next(g)
    g.send(g)
    self.assertGreater(sys.getrefcount(g), 2)
    self.assertFalse(finalized)
    del g
    support.gc_collect()
    self.assertTrue(finalized)
    self.assertEqual(gc.garbage, old_garbage)
