# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_close_and_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pair = self.tp(self.MockRawIO(), self.MockRawIO())
    self.assertFalse(pair.closed)
    pair.close()
    self.assertTrue(pair.closed)
