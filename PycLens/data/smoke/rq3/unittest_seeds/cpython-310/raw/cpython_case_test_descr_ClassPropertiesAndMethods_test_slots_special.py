# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_slots_special

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class D(object):
        __slots__ = ['__dict__']
    a = D()
    self.assertHasAttr(a, '__dict__')
    self.assertNotHasAttr(a, '__weakref__')
    a.foo = 42
    self.assertEqual(a.__dict__, {'foo': 42})

    class W(object):
        __slots__ = ['__weakref__']
    a = W()
    self.assertHasAttr(a, '__weakref__')
    self.assertNotHasAttr(a, '__dict__')
    try:
        a.foo = 42
    except AttributeError:
        pass
    else:
        self.fail("shouldn't be allowed to set a.foo")

    class C1(W, D):
        __slots__ = []
    a = C1()
    self.assertHasAttr(a, '__dict__')
    self.assertHasAttr(a, '__weakref__')
    a.foo = 42
    self.assertEqual(a.__dict__, {'foo': 42})

    class C2(D, W):
        __slots__ = []
    a = C2()
    self.assertHasAttr(a, '__dict__')
    self.assertHasAttr(a, '__weakref__')
    a.foo = 42
    self.assertEqual(a.__dict__, {'foo': 42})
