# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ExceptionChainingTest_test_unflagged_non_text_codec_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def encode_to_str(*args, **kwds):
        return ('not bytes!', 0)

    def decode_to_bytes(*args, **kwds):
        return (b'not str!', 0)
    self.set_codec(encode_to_str, decode_to_bytes)
    encoded = codecs.encode(None, self.codec_name)
    self.assertEqual(encoded, 'not bytes!')
    decoded = codecs.decode(None, self.codec_name)
    self.assertEqual(decoded, b'not str!')
    fmt = "^{!r} encoder returned 'str' instead of 'bytes'; use codecs.encode\\(\\) to encode to arbitrary types$"
    msg = fmt.format(self.codec_name)
    with self.assertRaisesRegex(TypeError, msg):
        'str_input'.encode(self.codec_name)
    fmt = "^{!r} decoder returned 'bytes' instead of 'str'; use codecs.decode\\(\\) to decode to arbitrary types$"
    msg = fmt.format(self.codec_name)
    with self.assertRaisesRegex(TypeError, msg):
        b'bytes input'.decode(self.codec_name)
