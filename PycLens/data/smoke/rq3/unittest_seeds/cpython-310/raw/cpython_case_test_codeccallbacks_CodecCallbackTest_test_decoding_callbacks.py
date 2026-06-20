# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_decoding_callbacks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def relaxedutf8(exc):
        if not isinstance(exc, UnicodeDecodeError):
            raise TypeError("don't know how to handle %r" % exc)
        if exc.object[exc.start:exc.start + 2] == b'\xc0\x80':
            return ('\x00', exc.start + 2)
        else:
            raise exc
    codecs.register_error('test.relaxedutf8', relaxedutf8)
    sin = b'a\x00b\xc0\x80c\xc3\xbc\xc0\x80\xc0\x80'
    sout = 'a\x00b\x00cü\x00\x00'
    self.assertEqual(sin.decode('utf-8', 'test.relaxedutf8'), sout)
    sin = b'\xc0\x80\xc0\x81'
    self.assertRaises(UnicodeDecodeError, sin.decode, 'utf-8', 'test.relaxedutf8')
