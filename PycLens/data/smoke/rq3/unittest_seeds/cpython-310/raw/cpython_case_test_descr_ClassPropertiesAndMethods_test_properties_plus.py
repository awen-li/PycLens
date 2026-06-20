# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_properties_plus

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):
        foo = property(doc='hello')

        @foo.getter
        def foo(self):
            return self._foo

        @foo.setter
        def foo(self, value):
            self._foo = abs(value)

        @foo.deleter
        def foo(self):
            del self._foo
    c = C()
    self.assertEqual(C.foo.__doc__, 'hello')
    self.assertNotHasAttr(c, 'foo')
    c.foo = -42
    self.assertHasAttr(c, '_foo')
    self.assertEqual(c._foo, 42)
    self.assertEqual(c.foo, 42)
    del c.foo
    self.assertNotHasAttr(c, '_foo')
    self.assertNotHasAttr(c, 'foo')

    class D(C):

        @C.foo.deleter
        def foo(self):
            try:
                del self._foo
            except AttributeError:
                pass
    d = D()
    d.foo = 24
    self.assertEqual(d.foo, 24)
    del d.foo
    del d.foo

    class E(object):

        @property
        def foo(self):
            return self._foo

        @foo.setter
        def foo(self, value):
            raise RuntimeError

        @foo.setter
        def foo(self, value):
            self._foo = abs(value)

        @foo.deleter
        def foo(self, value=None):
            del self._foo
    e = E()
    e.foo = -42
    self.assertEqual(e.foo, 42)
    del e.foo

    class F(E):

        @E.foo.deleter
        def foo(self):
            del self._foo

        @foo.setter
        def foo(self, value):
            self._foo = max(0, value)
    f = F()
    f.foo = -10
    self.assertEqual(f.foo, 0)
    del f.foo
