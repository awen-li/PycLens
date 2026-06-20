# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_classic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def foo(*a):
            return a
        goo = classmethod(foo)
    c = C()
    self.assertEqual(C.goo(1), (C, 1))
    self.assertEqual(c.goo(1), (C, 1))
    self.assertEqual(c.foo(1), (c, 1))

    class D(C):
        pass
    d = D()
    self.assertEqual(D.goo(1), (D, 1))
    self.assertEqual(d.goo(1), (D, 1))
    self.assertEqual(d.foo(1), (d, 1))
    self.assertEqual(D.foo(d, 1), (d, 1))

    class E:
        foo = C.foo
    self.assertEqual(E().foo.__func__, C.foo)
    self.assertTrue(repr(C.foo.__get__(C())).startswith('<bound method '))
