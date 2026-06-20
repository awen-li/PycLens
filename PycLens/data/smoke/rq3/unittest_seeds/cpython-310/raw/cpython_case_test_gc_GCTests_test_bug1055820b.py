# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_bug1055820b

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ouch = []

    def callback(ignored):
        ouch[:] = [wr() for wr in WRs]
    Cs = [C1055820(i) for i in range(2)]
    WRs = [weakref.ref(c, callback) for c in Cs]
    c = None
    gc.collect()
    self.assertEqual(len(ouch), 0)
    Cs = None
    gc.collect()
    self.assertEqual(len(ouch), 2)
    for x in ouch:
        self.assertEqual(x, None)
