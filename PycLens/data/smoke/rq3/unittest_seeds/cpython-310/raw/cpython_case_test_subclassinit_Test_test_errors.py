# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyMeta(type):
        pass
    with self.assertRaises(TypeError):

        class MyClass(metaclass=MyMeta, otherarg=1):
            pass
    with self.assertRaises(TypeError):
        types.new_class('MyClass', (object,), dict(metaclass=MyMeta, otherarg=1))
    types.prepare_class('MyClass', (object,), dict(metaclass=MyMeta, otherarg=1))

    class MyMeta(type):

        def __init__(self, name, bases, namespace, otherarg):
            super().__init__(name, bases, namespace)
    with self.assertRaises(TypeError):

        class MyClass(metaclass=MyMeta, otherarg=1):
            pass

    class MyMeta(type):

        def __new__(cls, name, bases, namespace, otherarg):
            return super().__new__(cls, name, bases, namespace)

        def __init__(self, name, bases, namespace, otherarg):
            super().__init__(name, bases, namespace)
            self.otherarg = otherarg

    class MyClass(metaclass=MyMeta, otherarg=1):
        pass
    self.assertEqual(MyClass.otherarg, 1)
