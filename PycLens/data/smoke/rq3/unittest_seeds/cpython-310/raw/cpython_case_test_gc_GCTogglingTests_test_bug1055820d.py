# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTogglingTests_test_bug1055820d

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ouch = []

    class D(C1055820):

        def __del__(self):
            ouch[:] = [c2wr()]
    d0 = D(0)
    gc.collect()
    c1 = C1055820(1)
    c1.keep_d0_alive = d0
    del d0.loop
    c2 = C1055820(2)
    c2wr = weakref.ref(c2)
    d0 = c1 = c2 = None
    detector = GC_Detector()
    junk = []
    i = 0
    while not detector.gc_happened:
        i += 1
        if i > 10000:
            self.fail("gc didn't happen after 10000 iterations")
        self.assertEqual(len(ouch), 0)
        junk.append([])
    self.assertEqual(len(ouch), 1)
    for x in ouch:
        self.assertEqual(x, None)
