# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IncrementalNewlineDecoderTest_test_newline_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _check(dec):
        self.assertEqual(dec.newlines, None)
        self.assertEqual(dec.decode('ഀ'), 'ഀ')
        self.assertEqual(dec.newlines, None)
        self.assertEqual(dec.decode('\u0a00'), '\u0a00')
        self.assertEqual(dec.newlines, None)
    dec = self.IncrementalNewlineDecoder(None, translate=False)
    _check(dec)
    dec = self.IncrementalNewlineDecoder(None, translate=True)
    _check(dec)
