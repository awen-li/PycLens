# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_bad_new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, object.__new__)
    self.assertRaises(TypeError, object.__new__, '')
    self.assertRaises(TypeError, list.__new__, object)
    self.assertRaises(TypeError, object.__new__, list)

    class C(object):
        __new__ = list.__new__
    self.assertRaises(TypeError, C)

    class C(list):
        __new__ = object.__new__
    self.assertRaises(TypeError, C)
