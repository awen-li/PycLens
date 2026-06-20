# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_newinstance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):
        pass
    a = A()
    a.a = a
    gc.collect()
    del a
    self.assertNotEqual(gc.collect(), 0)

    class B(list):
        pass

    class C(B, A):
        pass
    a = C()
    a.a = a
    gc.collect()
    del a
    self.assertNotEqual(gc.collect(), 0)
    del B, C
    self.assertNotEqual(gc.collect(), 0)
    A.a = A()
    del A
    self.assertNotEqual(gc.collect(), 0)
    self.assertEqual(gc.collect(), 0)
