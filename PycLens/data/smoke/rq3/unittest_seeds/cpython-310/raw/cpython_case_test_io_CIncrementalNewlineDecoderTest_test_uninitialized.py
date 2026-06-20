# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CIncrementalNewlineDecoderTest_test_uninitialized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    uninitialized = self.IncrementalNewlineDecoder.__new__(self.IncrementalNewlineDecoder)
    self.assertRaises(ValueError, uninitialized.decode, b'bar')
    self.assertRaises(ValueError, uninitialized.getstate)
    self.assertRaises(ValueError, uninitialized.setstate, (b'foo', 0))
    self.assertRaises(ValueError, uninitialized.reset)
