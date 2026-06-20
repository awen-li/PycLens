# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_sf_bug_840829

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import gc

    class C(object):
        pass
    c = C()
    wr = weakref.ref(c, lambda ignore: gc.collect())
    del c
    del wr
    c1 = C()
    c1.i = C()
    wr = weakref.ref(c1.i, lambda ignore: gc.collect())
    c2 = C()
    c2.c1 = c1
    del c1
    del c2
