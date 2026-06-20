# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CommonBufferedTests_test_invalid_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockRawIO()
    bufio = self.tp(rawio)
    self.assertRaises(ValueError, bufio.seek, 0, -1)
    self.assertRaises(ValueError, bufio.seek, 0, 9)
