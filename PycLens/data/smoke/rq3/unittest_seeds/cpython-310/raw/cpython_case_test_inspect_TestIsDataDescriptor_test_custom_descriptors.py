# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestIsDataDescriptor_test_custom_descriptors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NonDataDescriptor:

        def __get__(self, value, type=None):
            pass

    class DataDescriptor0:

        def __set__(self, name, value):
            pass

    class DataDescriptor1:

        def __delete__(self, name):
            pass

    class DataDescriptor2:
        __set__ = None
    self.assertFalse(inspect.isdatadescriptor(NonDataDescriptor()), 'class with only __get__ not a data descriptor')
    self.assertTrue(inspect.isdatadescriptor(DataDescriptor0()), 'class with __set__ is a data descriptor')
    self.assertTrue(inspect.isdatadescriptor(DataDescriptor1()), 'class with __delete__ is a data descriptor')
    self.assertTrue(inspect.isdatadescriptor(DataDescriptor2()), 'class with __set__ = None is a data descriptor')
