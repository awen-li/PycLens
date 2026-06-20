# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalDecoder_test_iso2022

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decoder = codecs.getincrementaldecoder('iso2022-jp')()
    ESC = b'\x1b'
    self.assertEqual(decoder.decode(ESC + b'('), '')
    self.assertEqual(decoder.decode(b'B', True), '')
    self.assertEqual(decoder.decode(ESC + b'$'), '')
    self.assertEqual(decoder.decode(b'B@$'), '世')
    self.assertEqual(decoder.decode(b'@$@'), '世')
    self.assertEqual(decoder.decode(b'$', True), '世')
    self.assertEqual(decoder.reset(), None)
    self.assertEqual(decoder.decode(b'@$'), '@$')
    self.assertEqual(decoder.decode(ESC + b'$'), '')
    self.assertRaises(UnicodeDecodeError, decoder.decode, b'', True)
    self.assertEqual(decoder.decode(b'B@$'), '世')
