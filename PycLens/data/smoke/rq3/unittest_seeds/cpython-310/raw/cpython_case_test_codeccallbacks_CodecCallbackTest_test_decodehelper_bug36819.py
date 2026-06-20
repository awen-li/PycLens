# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_decodehelper_bug36819

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = RepeatedPosReturn('x')
    codecs.register_error('test.bug36819', handler.handle)
    testcases = [('ascii', b'\xff'), ('utf-8', b'\xff'), ('utf-16be', b'\xdc\x80'), ('utf-32be', b'\x00\x00\xdc\x80'), ('iso-8859-6', b'\xff')]
    for (enc, bad) in testcases:
        input = 'abcd'.encode(enc) + bad
        with self.subTest(encoding=enc):
            handler.count = 50
            decoded = input.decode(enc, 'test.bug36819')
            self.assertEqual(decoded, 'abcdx' * 51)
