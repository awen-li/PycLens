# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_callback_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = Object(1)
    callback = lambda ref: None
    ref1 = weakref.ref(x, callback)
    self.assertIs(ref1.__callback__, callback)
    ref2 = weakref.ref(x)
    self.assertIsNone(ref2.__callback__)
