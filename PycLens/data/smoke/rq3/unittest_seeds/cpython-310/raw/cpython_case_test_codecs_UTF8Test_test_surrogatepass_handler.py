# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF8Test_test_surrogatepass_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('abc\ud800def'.encode(self.encoding, 'surrogatepass'), self.BOM + b'abc\xed\xa0\x80def')
    self.assertEqual('\U00010fff\ud800'.encode(self.encoding, 'surrogatepass'), self.BOM + b'\xf0\x90\xbf\xbf\xed\xa0\x80')
    self.assertEqual('[\ud800\udc80]'.encode(self.encoding, 'surrogatepass'), self.BOM + b'[\xed\xa0\x80\xed\xb2\x80]')
    self.assertEqual(b'abc\xed\xa0\x80def'.decode(self.encoding, 'surrogatepass'), 'abc\ud800def')
    self.assertEqual(b'\xf0\x90\xbf\xbf\xed\xa0\x80'.decode(self.encoding, 'surrogatepass'), '\U00010fff\ud800')
    self.assertTrue(codecs.lookup_error('surrogatepass'))
    with self.assertRaises(UnicodeDecodeError):
        b'abc\xed\xa0'.decode(self.encoding, 'surrogatepass')
    with self.assertRaises(UnicodeDecodeError):
        b'abc\xed\xa0z'.decode(self.encoding, 'surrogatepass')
