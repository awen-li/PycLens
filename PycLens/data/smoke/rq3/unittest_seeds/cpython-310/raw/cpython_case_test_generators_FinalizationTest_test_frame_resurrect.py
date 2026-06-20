# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: FinalizationTest_test_frame_resurrect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen():
        nonlocal frame
        try:
            yield
        finally:
            frame = sys._getframe()
    g = gen()
    wr = weakref.ref(g)
    next(g)
    del g
    support.gc_collect()
    self.assertIs(wr(), None)
    self.assertTrue(frame)
    del frame
    support.gc_collect()
