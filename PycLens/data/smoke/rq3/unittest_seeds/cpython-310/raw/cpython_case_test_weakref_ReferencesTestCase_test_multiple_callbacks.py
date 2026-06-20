# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_multiple_callbacks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = C()
    ref1 = weakref.ref(o, self.callback)
    ref2 = weakref.ref(o, self.callback)
    del o
    gc_collect()
    self.assertIsNone(ref1(), 'expected reference to be invalidated')
    self.assertIsNone(ref2(), 'expected reference to be invalidated')
    self.assertEqual(self.cbcalled, 2, 'callback not called the right number of times')
