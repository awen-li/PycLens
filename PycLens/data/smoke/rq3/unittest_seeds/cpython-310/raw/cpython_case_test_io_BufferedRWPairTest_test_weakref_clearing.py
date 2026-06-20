# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_weakref_clearing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    brw = self.tp(self.MockRawIO(), self.MockRawIO())
    ref = weakref.ref(brw)
    brw = None
    ref = None
