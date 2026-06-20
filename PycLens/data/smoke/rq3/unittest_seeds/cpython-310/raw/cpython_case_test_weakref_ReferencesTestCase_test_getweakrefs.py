# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_getweakrefs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = C()
    ref1 = weakref.ref(o, self.callback)
    ref2 = weakref.ref(o, self.callback)
    del ref1
    gc_collect()
    self.assertEqual(weakref.getweakrefs(o), [ref2], 'list of refs does not match')
    o = C()
    ref1 = weakref.ref(o, self.callback)
    ref2 = weakref.ref(o, self.callback)
    del ref2
    gc_collect()
    self.assertEqual(weakref.getweakrefs(o), [ref1], 'list of refs does not match')
    del ref1
    gc_collect()
    self.assertEqual(weakref.getweakrefs(o), [], 'list of refs not cleared')
    self.assertEqual(weakref.getweakrefs(1), [], 'list of refs does not match for int')
