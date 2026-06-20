# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_getweakrefcount

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = C()
    ref1 = weakref.ref(o)
    ref2 = weakref.ref(o, self.callback)
    self.assertEqual(weakref.getweakrefcount(o), 2, 'got wrong number of weak reference objects')
    proxy1 = weakref.proxy(o)
    proxy2 = weakref.proxy(o, self.callback)
    self.assertEqual(weakref.getweakrefcount(o), 4, 'got wrong number of weak reference objects')
    del ref1, ref2, proxy1, proxy2
    gc_collect()
    self.assertEqual(weakref.getweakrefcount(o), 0, 'weak reference objects not unlinked from referent when discarded.')
    self.assertEqual(weakref.getweakrefcount(1), 0, 'got wrong number of weak reference objects for int')
