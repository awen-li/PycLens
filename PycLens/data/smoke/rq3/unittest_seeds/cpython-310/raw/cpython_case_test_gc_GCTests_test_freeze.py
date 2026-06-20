# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_freeze

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gc.freeze()
    self.assertGreater(gc.get_freeze_count(), 0)
    gc.unfreeze()
    self.assertEqual(gc.get_freeze_count(), 0)
