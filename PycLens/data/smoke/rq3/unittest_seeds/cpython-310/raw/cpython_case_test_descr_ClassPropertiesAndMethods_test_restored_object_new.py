# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_restored_object_new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):

        def __new__(cls, *args, **kwargs):
            raise AssertionError
    self.assertRaises(AssertionError, A)

    class B(A):
        __new__ = object.__new__

        def __init__(self, foo):
            self.foo = foo
    with warnings.catch_warnings():
        warnings.simplefilter('error', DeprecationWarning)
        b = B(3)
    self.assertEqual(b.foo, 3)
    self.assertEqual(b.__class__, B)
    del B.__new__
    self.assertRaises(AssertionError, B)
    del A.__new__
    with warnings.catch_warnings():
        warnings.simplefilter('error', DeprecationWarning)
        b = B(3)
    self.assertEqual(b.foo, 3)
    self.assertEqual(b.__class__, B)
