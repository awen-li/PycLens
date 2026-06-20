# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_dynamics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class D(object):
        pass

    class E(D):
        pass

    class F(D):
        pass
    D.foo = 1
    self.assertEqual(D.foo, 1)
    self.assertEqual(E.foo, 1)
    self.assertEqual(F.foo, 1)

    class C(object):
        pass
    a = C()
    self.assertNotHasAttr(a, 'foobar')
    C.foobar = 2
    self.assertEqual(a.foobar, 2)
    C.method = lambda self: 42
    self.assertEqual(a.method(), 42)
    C.__repr__ = lambda self: 'C()'
    self.assertEqual(repr(a), 'C()')
    C.__int__ = lambda self: 100
    self.assertEqual(int(a), 100)
    self.assertEqual(a.foobar, 2)
    self.assertNotHasAttr(a, 'spam')

    def mygetattr(self, name):
        if name == 'spam':
            return 'spam'
        raise AttributeError
    C.__getattr__ = mygetattr
    self.assertEqual(a.spam, 'spam')
    a.new = 12
    self.assertEqual(a.new, 12)

    def mysetattr(self, name, value):
        if name == 'spam':
            raise AttributeError
        return object.__setattr__(self, name, value)
    C.__setattr__ = mysetattr
    try:
        a.spam = 'not spam'
    except AttributeError:
        pass
    else:
        self.fail('expected AttributeError')
    self.assertEqual(a.spam, 'spam')

    class D(C):
        pass
    d = D()
    d.foo = 1
    self.assertEqual(d.foo, 1)

    class I(int):
        pass
    self.assertEqual('a' * I(2), 'aa')
    self.assertEqual(I(2) * 'a', 'aa')
    self.assertEqual(2 * I(3), 6)
    self.assertEqual(I(3) * 2, 6)
    self.assertEqual(I(3) * I(2), 6)

    class dynamicmetaclass(type):
        pass

    class someclass(metaclass=dynamicmetaclass):
        pass
    self.assertNotEqual(someclass, object)
