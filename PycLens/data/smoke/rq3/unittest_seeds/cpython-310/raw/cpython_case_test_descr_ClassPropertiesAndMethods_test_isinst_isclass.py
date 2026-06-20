# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_isinst_isclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Proxy(object):

        def __init__(self, obj):
            self.__obj = obj

        def __getattribute__(self, name):
            if name.startswith('_Proxy__'):
                return object.__getattribute__(self, name)
            else:
                return getattr(self.__obj, name)

    class C:
        pass
    a = C()
    pa = Proxy(a)
    self.assertIsInstance(a, C)
    self.assertIsInstance(pa, C)

    class D(C):
        pass
    a = D()
    pa = Proxy(a)
    self.assertIsInstance(a, C)
    self.assertIsInstance(pa, C)

    class C(object):
        pass
    a = C()
    pa = Proxy(a)
    self.assertIsInstance(a, C)
    self.assertIsInstance(pa, C)

    class D(C):
        pass
    a = D()
    pa = Proxy(a)
    self.assertIsInstance(a, C)
    self.assertIsInstance(pa, C)
