# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dynamicclassattribute.py
# case: PropertyTests_test_property_decorator_baseclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = BaseClass()
    self.assertEqual(base.spam, 5)
    self.assertEqual(base._spam, 5)
    base.spam = 10
    self.assertEqual(base.spam, 10)
    self.assertEqual(base._spam, 10)
    delattr(base, 'spam')
    self.assertTrue(not hasattr(base, 'spam'))
    self.assertTrue(not hasattr(base, '_spam'))
    base.spam = 20
    self.assertEqual(base.spam, 20)
    self.assertEqual(base._spam, 20)
