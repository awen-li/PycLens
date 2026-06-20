# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_encodehelper_bug36819

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = RepeatedPosReturn()
    codecs.register_error('test.bug36819', handler.handle)
    input = 'abcd\udc80'
    encodings = ['ascii', 'latin1', 'utf-8', 'utf-16', 'utf-32']
    encodings += ['iso-8859-15']
    if sys.platform == 'win32':
        encodings = ['mbcs', 'oem']
    handler.repl = '\udcff'
    for enc in encodings:
        with self.subTest(encoding=enc):
            handler.count = 50
            with self.assertRaises(UnicodeEncodeError) as cm:
                input.encode(enc, 'test.bug36819')
            exc = cm.exception
            self.assertEqual(exc.start, 4)
            self.assertEqual(exc.end, 5)
            self.assertEqual(exc.object, input)
    if sys.platform == 'win32':
        handler.count = 50
        with self.assertRaises(UnicodeEncodeError) as cm:
            codecs.code_page_encode(437, input, 'test.bug36819')
        exc = cm.exception
        self.assertEqual(exc.start, 4)
        self.assertEqual(exc.end, 5)
        self.assertEqual(exc.object, input)
    handler.repl = 'x'
    for enc in encodings:
        with self.subTest(encoding=enc):
            handler.count = 50
            encoded = input.encode(enc, 'test.bug36819')
            self.assertEqual(encoded.decode(enc), 'abcdx' * 51)
    if sys.platform == 'win32':
        handler.count = 50
        encoded = codecs.code_page_encode(437, input, 'test.bug36819')
        self.assertEqual(encoded[0].decode(), 'abcdx' * 51)
        self.assertEqual(encoded[1], len(input))
