# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_staticmethods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def foo(*a):
            return a
        goo = staticmethod(foo)
    c = C()
    self.assertEqual(C.goo(1), (1,))
    self.assertEqual(c.goo(1), (1,))
    self.assertEqual(c.foo(1), (c, 1))

    class D(C):
        pass
    d = D()
    self.assertEqual(D.goo(1), (1,))
    self.assertEqual(d.goo(1), (1,))
    self.assertEqual(d.foo(1), (d, 1))
    self.assertEqual(D.foo(d, 1), (d, 1))
    sm = staticmethod(None)
    self.assertEqual(sm.__dict__, {'__doc__': None})
    sm.x = 42
    self.assertEqual(sm.x, 42)
    self.assertEqual(sm.__dict__, {'x': 42, '__doc__': None})
    del sm.x
    self.assertNotHasAttr(sm, 'x')
