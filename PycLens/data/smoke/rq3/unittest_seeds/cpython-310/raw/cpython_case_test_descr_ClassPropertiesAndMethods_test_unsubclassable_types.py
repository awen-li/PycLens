# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_unsubclassable_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):

        class X(type(None)):
            pass
    with self.assertRaises(TypeError):

        class X(object, type(None)):
            pass
    with self.assertRaises(TypeError):

        class X(type(None), object):
            pass

    class O(object):
        pass
    with self.assertRaises(TypeError):

        class X(O, type(None)):
            pass
    with self.assertRaises(TypeError):

        class X(type(None), O):
            pass

    class X(object):
        pass
    with self.assertRaises(TypeError):
        X.__bases__ = (type(None),)
    with self.assertRaises(TypeError):
        X.__bases__ = (object, type(None))
    with self.assertRaises(TypeError):
        X.__bases__ = (type(None), object)
    with self.assertRaises(TypeError):
        X.__bases__ = (O, type(None))
    with self.assertRaises(TypeError):
        X.__bases__ = (type(None), O)
