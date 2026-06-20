# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_is_finalized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(gc.is_finalized(3))
    storage = []

    class Lazarus:

        def __del__(self):
            storage.append(self)
    lazarus = Lazarus()
    self.assertFalse(gc.is_finalized(lazarus))
    del lazarus
    gc.collect()
    lazarus = storage.pop()
    self.assertTrue(gc.is_finalized(lazarus))
