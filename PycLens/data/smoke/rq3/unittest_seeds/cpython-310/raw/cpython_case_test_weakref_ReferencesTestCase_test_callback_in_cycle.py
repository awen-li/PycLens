# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_callback_in_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import gc

    class J(object):
        pass

    class II(object):

        def acallback(self, ignore):
            self.J
    I = II()
    I.J = J
    I.wr = weakref.ref(J, I.acallback)
    del I, J, II
    gc.collect()
