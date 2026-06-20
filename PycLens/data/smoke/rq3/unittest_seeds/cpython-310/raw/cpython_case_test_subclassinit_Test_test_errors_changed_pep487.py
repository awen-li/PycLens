# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_errors_changed_pep487

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyMeta(type):

        def __new__(cls, name, bases, namespace):
            return super().__new__(cls, name=name, bases=bases, dict=namespace)
    with self.assertRaises(TypeError):

        class MyClass(metaclass=MyMeta):
            pass

    class MyMeta(type):

        def __new__(cls, name, bases, namespace, otherarg):
            self = super().__new__(cls, name, bases, namespace)
            self.otherarg = otherarg
            return self

    class MyClass(metaclass=MyMeta, otherarg=1):
        pass
    self.assertEqual(MyClass.otherarg, 1)
