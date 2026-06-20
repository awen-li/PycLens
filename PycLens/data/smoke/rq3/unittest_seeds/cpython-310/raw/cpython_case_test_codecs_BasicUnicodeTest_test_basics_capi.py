# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: BasicUnicodeTest_test_basics_capi

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'abc123'
    for encoding in all_unicode_encodings:
        if encoding not in broken_unicode_with_stateful:
            try:
                cencoder = _testcapi.codec_incrementalencoder(encoding)
            except LookupError:
                pass
            else:
                encodedresult = b''
                for c in s:
                    encodedresult += cencoder.encode(c)
                encodedresult += cencoder.encode('', True)
                cdecoder = _testcapi.codec_incrementaldecoder(encoding)
                decodedresult = ''
                for c in encodedresult:
                    decodedresult += cdecoder.decode(bytes([c]))
                decodedresult += cdecoder.decode(b'', True)
                self.assertEqual(decodedresult, s, 'encoding=%r' % encoding)
            if encoding not in ('idna', 'mbcs'):
                try:
                    cencoder = _testcapi.codec_incrementalencoder(encoding, 'ignore')
                except LookupError:
                    pass
                else:
                    encodedresult = b''.join((cencoder.encode(c) for c in s))
                    cdecoder = _testcapi.codec_incrementaldecoder(encoding, 'ignore')
                    decodedresult = ''.join((cdecoder.decode(bytes([c])) for c in encodedresult))
                    self.assertEqual(decodedresult, s, 'encoding=%r' % encoding)
