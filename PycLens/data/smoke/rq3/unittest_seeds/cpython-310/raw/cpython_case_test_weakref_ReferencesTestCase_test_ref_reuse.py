# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_ref_reuse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = C()
    ref1 = weakref.ref(o)
    proxy = weakref.proxy(o)
    ref2 = weakref.ref(o)
    self.assertIs(ref1, ref2, 'reference object w/out callback should be re-used')
    o = C()
    proxy = weakref.proxy(o)
    ref1 = weakref.ref(o)
    ref2 = weakref.ref(o)
    self.assertIs(ref1, ref2, 'reference object w/out callback should be re-used')
    self.assertEqual(weakref.getweakrefcount(o), 2, 'wrong weak ref count for object')
    del proxy
    gc_collect()
    self.assertEqual(weakref.getweakrefcount(o), 1, 'wrong weak ref count for object after deleting proxy')
