# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pair = self.tp(self.BytesIO(b'abcdef'), self.MockRawIO())
    self.assertEqual(pair.read(3), b'abc')
    self.assertEqual(pair.read(1), b'd')
    self.assertEqual(pair.read(), b'ef')
    pair = self.tp(self.BytesIO(b'abc'), self.MockRawIO())
    self.assertEqual(pair.read(None), b'abc')
