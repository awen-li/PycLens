# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_object_new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):
        pass
    object.__new__(A)
    self.assertRaises(TypeError, object.__new__, A, 5)
    object.__init__(A())
    self.assertRaises(TypeError, object.__init__, A(), 5)

    class A(object):

        def __init__(self, foo):
            self.foo = foo
    object.__new__(A)
    object.__new__(A, 5)
    object.__init__(A(3))
    self.assertRaises(TypeError, object.__init__, A(3), 5)

    class A(object):

        def __new__(cls, foo):
            return object.__new__(cls)
    object.__new__(A)
    self.assertRaises(TypeError, object.__new__, A, 5)
    object.__init__(A(3))
    object.__init__(A(3), 5)

    class A(object):

        def __new__(cls, foo):
            return object.__new__(cls)

        def __init__(self, foo):
            self.foo = foo
    object.__new__(A)
    self.assertRaises(TypeError, object.__new__, A, 5)
    object.__init__(A(3))
    self.assertRaises(TypeError, object.__init__, A(3), 5)
