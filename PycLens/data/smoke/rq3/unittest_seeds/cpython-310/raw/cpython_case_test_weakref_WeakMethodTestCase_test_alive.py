# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: WeakMethodTestCase_test_alive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = Object(1)
    r = weakref.WeakMethod(o.some_method)
    self.assertIsInstance(r, weakref.ReferenceType)
    self.assertIsInstance(r(), type(o.some_method))
    self.assertIs(r().__self__, o)
    self.assertIs(r().__func__, o.some_method.__func__)
    self.assertEqual(r()(), 4)
