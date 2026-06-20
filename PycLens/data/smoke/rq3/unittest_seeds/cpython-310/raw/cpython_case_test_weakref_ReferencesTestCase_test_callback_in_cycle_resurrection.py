# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_callback_in_cycle_resurrection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import gc
    alist = []

    class C(object):

        def __init__(self, value):
            self.attribute = value

        def acallback(self, ignore):
            alist.append(self.c)
    (c1, c2) = (C(1), C(2))
    c1.c = c2
    c2.c = c1
    c1.wr = weakref.ref(c2, c1.acallback)
    c2.wr = weakref.ref(c1, c2.acallback)

    def C_went_away(ignore):
        alist.append('C went away')
    wr = weakref.ref(C, C_went_away)
    del c1, c2, C
    self.assertEqual(alist, [])
    gc.collect()
    self.assertEqual(alist, ['C went away'])
    self.assertEqual(wr(), None)
    del alist[:]
    gc.collect()
    self.assertEqual(alist, [])
