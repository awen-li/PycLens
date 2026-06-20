# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dynamicclassattribute.py
# case: PropertyTests_test_property_decorator_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sub = SubClass()
    self.assertRaises(PropertyGet, getattr, sub, 'spam')
    self.assertRaises(PropertySet, setattr, sub, 'spam', None)
    self.assertRaises(PropertyDel, delattr, sub, 'spam')
