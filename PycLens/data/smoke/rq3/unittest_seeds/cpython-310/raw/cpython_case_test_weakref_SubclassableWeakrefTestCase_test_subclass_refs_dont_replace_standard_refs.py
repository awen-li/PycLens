# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: SubclassableWeakrefTestCase_test_subclass_refs_dont_replace_standard_refs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyRef(weakref.ref):
        pass
    o = Object(42)
    r1 = MyRef(o)
    r2 = weakref.ref(o)
    self.assertIsNot(r1, r2)
    self.assertEqual(weakref.getweakrefs(o), [r2, r1])
    self.assertEqual(weakref.getweakrefcount(o), 2)
    r3 = MyRef(o)
    self.assertEqual(weakref.getweakrefcount(o), 3)
    refs = weakref.getweakrefs(o)
    self.assertEqual(len(refs), 3)
    self.assertIs(r2, refs[0])
    self.assertIn(r1, refs[1:])
    self.assertIn(r3, refs[1:])
