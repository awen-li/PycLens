# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_encode_bytes_replacement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def handle(exc):
        if isinstance(exc, UnicodeEncodeError):
            return (repl, exc.end)
        raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error('test.replacing', handle)
    for (enc, input, repl) in (('ascii', '[¤]', b'\xbd\xbe'), ('iso-8859-1', '[€]', b'\xbd\xbe'), ('iso-8859-15', '[¤]', b'\xbd\xbe'), ('utf-8', '[\udc80]', b'\xbd\xbe'), ('utf-16le', '[\udc80]', b'\xbd\xbe'), ('utf-16be', '[\udc80]', b'\xbd\xbe'), ('utf-32le', '[\udc80]', b'\xbc\xbd\xbe\xbf'), ('utf-32be', '[\udc80]', b'\xbc\xbd\xbe\xbf')):
        with self.subTest(encoding=enc):
            res = input.encode(enc, 'test.replacing')
            self.assertEqual(res, '['.encode(enc) + repl + ']'.encode(enc))
