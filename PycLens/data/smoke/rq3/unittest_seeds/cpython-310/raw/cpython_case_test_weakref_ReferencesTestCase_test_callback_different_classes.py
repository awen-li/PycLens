# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_callback_different_classes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import gc

    class C(object):

        def cb(self, ignore):
            self.me
            self.c1
            self.wr

    class D:
        pass
    (c1, c2) = (D(), C())
    c2.me = c2
    c2.c1 = c1
    c2.wr = weakref.ref(c1, c2.cb)
    del c1, c2, C, D
    gc.collect()
