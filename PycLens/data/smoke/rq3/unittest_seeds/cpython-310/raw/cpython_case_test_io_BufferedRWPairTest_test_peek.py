# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_peek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pair = self.tp(self.BytesIO(b'abcdef'), self.MockRawIO())
    self.assertTrue(pair.peek(3).startswith(b'abc'))
    self.assertEqual(pair.read(3), b'abc')
