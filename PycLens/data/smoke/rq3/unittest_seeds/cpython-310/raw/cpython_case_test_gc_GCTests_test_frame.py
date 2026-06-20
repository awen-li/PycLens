# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_frame

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        frame = sys._getframe()
    gc.collect()
    f()
    self.assertEqual(gc.collect(), 1)
