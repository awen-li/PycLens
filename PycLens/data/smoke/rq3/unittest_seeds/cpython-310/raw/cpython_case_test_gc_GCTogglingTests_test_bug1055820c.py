# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTogglingTests_test_bug1055820c

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c0 = C1055820(0)
    gc.collect()
    c1 = C1055820(1)
    c1.keep_c0_alive = c0
    del c0.loop
    c2 = C1055820(2)
    c2wr = weakref.ref(c2)
    ouch = []

    def callback(ignored):
        ouch[:] = [c2wr()]
    c0wr = weakref.ref(c0, callback)
    c0 = c1 = c2 = None
    junk = []
    i = 0
    detector = GC_Detector()
    while not detector.gc_happened:
        i += 1
        if i > 10000:
            self.fail("gc didn't happen after 10000 iterations")
        self.assertEqual(len(ouch), 0)
        junk.append([])
    self.assertEqual(len(ouch), 1)
    for x in ouch:
        self.assertEqual(x, None)
