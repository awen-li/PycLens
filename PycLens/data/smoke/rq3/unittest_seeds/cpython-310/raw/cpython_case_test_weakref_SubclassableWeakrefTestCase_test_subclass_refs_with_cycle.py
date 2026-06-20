# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: SubclassableWeakrefTestCase_test_subclass_refs_with_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyRef(weakref.ref):
        pass

    def callback(w):
        self.cbcalled += 1
    o = C()
    r1 = MyRef(o, callback)
    r1.o = o
    del o
    del r1
    self.assertEqual(self.cbcalled, 0)
    o = C()
    r1 = MyRef(o, callback)
    r2 = MyRef(o, callback)
    r1.r = r2
    r2.o = o
    del o
    del r2
    del r1
    self.assertEqual(self.cbcalled, 0)
