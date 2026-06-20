# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_subclass_propagation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass
    d = D()
    orig_hash = hash(d)
    A.__hash__ = lambda self: 42
    self.assertEqual(hash(d), 42)
    C.__hash__ = lambda self: 314
    self.assertEqual(hash(d), 314)
    B.__hash__ = lambda self: 144
    self.assertEqual(hash(d), 144)
    D.__hash__ = lambda self: 100
    self.assertEqual(hash(d), 100)
    D.__hash__ = None
    self.assertRaises(TypeError, hash, d)
    del D.__hash__
    self.assertEqual(hash(d), 144)
    B.__hash__ = None
    self.assertRaises(TypeError, hash, d)
    del B.__hash__
    self.assertEqual(hash(d), 314)
    C.__hash__ = None
    self.assertRaises(TypeError, hash, d)
    del C.__hash__
    self.assertEqual(hash(d), 42)
    A.__hash__ = None
    self.assertRaises(TypeError, hash, d)
    del A.__hash__
    self.assertEqual(hash(d), orig_hash)
    d.foo = 42
    d.bar = 42
    self.assertEqual(d.foo, 42)
    self.assertEqual(d.bar, 42)

    def __getattribute__(self, name):
        if name == 'foo':
            return 24
        return object.__getattribute__(self, name)
    A.__getattribute__ = __getattribute__
    self.assertEqual(d.foo, 24)
    self.assertEqual(d.bar, 42)

    def __getattr__(self, name):
        if name in ('spam', 'foo', 'bar'):
            return 'hello'
        raise AttributeError(name)
    B.__getattr__ = __getattr__
    self.assertEqual(d.spam, 'hello')
    self.assertEqual(d.foo, 24)
    self.assertEqual(d.bar, 42)
    del A.__getattribute__
    self.assertEqual(d.foo, 42)
    del d.foo
    self.assertEqual(d.foo, 'hello')
    self.assertEqual(d.bar, 42)
    del B.__getattr__
    try:
        d.foo
    except AttributeError:
        pass
    else:
        self.fail('d.foo should be undefined now')

    class A(object):
        pass

    class B(A):
        pass
    del B
    support.gc_collect()
    A.__setitem__ = lambda *a: None
