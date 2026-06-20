# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __init__(self, x):
            self.x = x

        def foo(self):
            return self.x
    c1 = C(1)
    self.assertEqual(c1.foo(), 1)

    class D(C):
        boo = C.foo
        goo = c1.foo
    d2 = D(2)
    self.assertEqual(d2.foo(), 2)
    self.assertEqual(d2.boo(), 2)
    self.assertEqual(d2.goo(), 1)

    class E(object):
        foo = C.foo
    self.assertEqual(E().foo.__func__, C.foo)
    self.assertTrue(repr(C.foo.__get__(C(1))).startswith('<bound method '))
