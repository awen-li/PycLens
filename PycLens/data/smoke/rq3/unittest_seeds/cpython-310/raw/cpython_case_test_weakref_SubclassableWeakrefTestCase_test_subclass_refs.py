# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: SubclassableWeakrefTestCase_test_subclass_refs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyRef(weakref.ref):

        def __init__(self, ob, callback=None, value=42):
            self.value = value
            super().__init__(ob, callback)

        def __call__(self):
            self.called = True
            return super().__call__()
    o = Object('foo')
    mr = MyRef(o, value=24)
    self.assertIs(mr(), o)
    self.assertTrue(mr.called)
    self.assertEqual(mr.value, 24)
    del o
    gc_collect()
    self.assertIsNone(mr())
    self.assertTrue(mr.called)
