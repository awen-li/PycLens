# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: SubclassableWeakrefTestCase_test_subclass_refs_with_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyRef(weakref.ref):
        __slots__ = ('slot1', 'slot2')

        def __new__(type, ob, callback, slot1, slot2):
            return weakref.ref.__new__(type, ob, callback)

        def __init__(self, ob, callback, slot1, slot2):
            self.slot1 = slot1
            self.slot2 = slot2

        def meth(self):
            return self.slot1 + self.slot2
    o = Object(42)
    r = MyRef(o, None, 'abc', 'def')
    self.assertEqual(r.slot1, 'abc')
    self.assertEqual(r.slot2, 'def')
    self.assertEqual(r.meth(), 'abcdef')
    self.assertFalse(hasattr(r, '__dict__'))
