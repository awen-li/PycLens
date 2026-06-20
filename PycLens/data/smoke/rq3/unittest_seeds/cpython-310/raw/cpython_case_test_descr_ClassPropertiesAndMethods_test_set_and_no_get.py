# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_set_and_no_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Descr(object):

        def __init__(self, name):
            self.name = name

        def __set__(self, obj, value):
            obj.__dict__[self.name] = value
    descr = Descr('a')

    class X(object):
        a = descr
    x = X()
    self.assertIs(x.a, descr)
    x.a = 42
    self.assertEqual(x.a, 42)

    class Meta(type):
        pass

    class X(metaclass=Meta):
        pass
    X.a = 42
    Meta.a = Descr('a')
    self.assertEqual(X.a, 42)
