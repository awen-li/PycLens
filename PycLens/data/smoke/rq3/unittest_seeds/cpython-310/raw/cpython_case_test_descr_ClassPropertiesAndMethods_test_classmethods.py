# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_classmethods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

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

    def f(cls, arg):
        """f docstring"""
        return (cls, arg)
    ff = classmethod(f)
    self.assertEqual(ff.__get__(0, int)(42), (int, 42))
    self.assertEqual(ff.__get__(0)(42), (int, 42))
    self.assertEqual(C.goo.__self__, C)
    self.assertEqual(D.goo.__self__, D)
    self.assertEqual(super(D, D).goo.__self__, D)
    self.assertEqual(super(D, d).goo.__self__, D)
    self.assertEqual(super(D, D).goo(), (D,))
    self.assertEqual(super(D, d).goo(), (D,))
    meth = classmethod(1).__get__(1)
    self.assertRaises(TypeError, meth)
    try:
        classmethod(f, kw=1)
    except TypeError:
        pass
    else:
        self.fail("classmethod shouldn't accept keyword args")
    cm = classmethod(f)
    cm_dict = {'__annotations__': {}, '__doc__': 'f docstring', '__module__': __name__, '__name__': 'f', '__qualname__': f.__qualname__}
    self.assertEqual(cm.__dict__, cm_dict)
    cm.x = 42
    self.assertEqual(cm.x, 42)
    self.assertEqual(cm.__dict__, {'x': 42, **cm_dict})
    del cm.x
    self.assertNotHasAttr(cm, 'x')
