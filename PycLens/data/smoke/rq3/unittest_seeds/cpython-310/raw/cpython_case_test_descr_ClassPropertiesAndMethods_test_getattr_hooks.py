# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_getattr_hooks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Descriptor(object):
        counter = 0

        def __get__(self, obj, objtype=None):

            def getter(name):
                self.counter += 1
                raise AttributeError(name)
            return getter
    descr = Descriptor()

    class A(object):
        __getattribute__ = descr

    class B(object):
        __getattr__ = descr

    class C(object):
        __getattribute__ = descr
        __getattr__ = descr
    self.assertRaises(AttributeError, getattr, A(), 'attr')
    self.assertEqual(descr.counter, 1)
    self.assertRaises(AttributeError, getattr, B(), 'attr')
    self.assertEqual(descr.counter, 2)
    self.assertRaises(AttributeError, getattr, C(), 'attr')
    self.assertEqual(descr.counter, 4)

    class EvilGetattribute(object):

        def __getattr__(self, name):
            raise AttributeError(name)

        def __getattribute__(self, name):
            del EvilGetattribute.__getattr__
            for i in range(5):
                gc.collect()
            raise AttributeError(name)
    self.assertRaises(AttributeError, getattr, EvilGetattribute(), 'attr')
