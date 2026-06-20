# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_overloading

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class B(object):
        """Intermediate class because object doesn't have a __setattr__"""

    class C(B):

        def __getattr__(self, name):
            if name == 'foo':
                return ('getattr', name)
            else:
                raise AttributeError

        def __setattr__(self, name, value):
            if name == 'foo':
                self.setattr = (name, value)
            else:
                return B.__setattr__(self, name, value)

        def __delattr__(self, name):
            if name == 'foo':
                self.delattr = name
            else:
                return B.__delattr__(self, name)

        def __getitem__(self, key):
            return ('getitem', key)

        def __setitem__(self, key, value):
            self.setitem = (key, value)

        def __delitem__(self, key):
            self.delitem = key
    a = C()
    self.assertEqual(a.foo, ('getattr', 'foo'))
    a.foo = 12
    self.assertEqual(a.setattr, ('foo', 12))
    del a.foo
    self.assertEqual(a.delattr, 'foo')
    self.assertEqual(a[12], ('getitem', 12))
    a[12] = 21
    self.assertEqual(a.setitem, (12, 21))
    del a[12]
    self.assertEqual(a.delitem, 12)
    self.assertEqual(a[0:10], ('getitem', slice(0, 10)))
    a[0:10] = 'foo'
    self.assertEqual(a.setitem, (slice(0, 10), 'foo'))
    del a[0:10]
    self.assertEqual(a.delitem, slice(0, 10))
