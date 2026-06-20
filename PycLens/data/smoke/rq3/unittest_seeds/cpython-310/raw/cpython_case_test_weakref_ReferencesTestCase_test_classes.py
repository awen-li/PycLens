# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_classes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):
        pass
    l = []
    weakref.ref(int)
    a = weakref.ref(A, l.append)
    A = None
    gc.collect()
    self.assertEqual(a(), None)
    self.assertEqual(l, [a])
