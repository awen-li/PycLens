# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_callback_attribute_after_deletion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = Object(1)
    ref = weakref.ref(x, self.callback)
    self.assertIsNotNone(ref.__callback__)
    del x
    support.gc_collect()
    self.assertIsNone(ref.__callback__)
