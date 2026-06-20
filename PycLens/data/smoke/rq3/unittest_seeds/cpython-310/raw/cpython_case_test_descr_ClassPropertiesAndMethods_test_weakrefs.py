# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_weakrefs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import weakref

    class C(object):
        pass
    c = C()
    r = weakref.ref(c)
    self.assertEqual(r(), c)
    del c
    support.gc_collect()
    self.assertEqual(r(), None)
    del r

    class NoWeak(object):
        __slots__ = ['foo']
    no = NoWeak()
    try:
        weakref.ref(no)
    except TypeError as msg:
        self.assertIn('weak reference', str(msg))
    else:
        self.fail('weakref.ref(no) should be illegal')

    class Weak(object):
        __slots__ = ['foo', '__weakref__']
    yes = Weak()
    r = weakref.ref(yes)
    self.assertEqual(r(), yes)
    del yes
    support.gc_collect()
    self.assertEqual(r(), None)
    del r
