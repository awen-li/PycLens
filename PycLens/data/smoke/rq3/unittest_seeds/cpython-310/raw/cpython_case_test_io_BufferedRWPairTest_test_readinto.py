# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_readinto

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for method in ('readinto', 'readinto1'):
        with self.subTest(method):
            pair = self.tp(self.BytesIO(b'abcdef'), self.MockRawIO())
            data = byteslike(b'\x00' * 5)
            self.assertEqual(getattr(pair, method)(data), 5)
            self.assertEqual(bytes(data), b'abcde')
