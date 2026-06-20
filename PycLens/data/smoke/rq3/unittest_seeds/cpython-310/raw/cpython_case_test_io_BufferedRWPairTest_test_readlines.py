# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_readlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pair = lambda : self.tp(self.BytesIO(b'abc\ndef\nh'), self.MockRawIO())
    self.assertEqual(pair().readlines(), [b'abc\n', b'def\n', b'h'])
    self.assertEqual(pair().readlines(), [b'abc\n', b'def\n', b'h'])
    self.assertEqual(pair().readlines(5), [b'abc\n', b'def\n'])
