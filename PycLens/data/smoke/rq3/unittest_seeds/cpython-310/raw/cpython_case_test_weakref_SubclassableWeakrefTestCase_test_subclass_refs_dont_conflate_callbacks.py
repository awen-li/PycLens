# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: SubclassableWeakrefTestCase_test_subclass_refs_dont_conflate_callbacks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyRef(weakref.ref):
        pass
    o = Object(42)
    r1 = MyRef(o, id)
    r2 = MyRef(o, str)
    self.assertIsNot(r1, r2)
    refs = weakref.getweakrefs(o)
    self.assertIn(r1, refs)
    self.assertIn(r2, refs)
