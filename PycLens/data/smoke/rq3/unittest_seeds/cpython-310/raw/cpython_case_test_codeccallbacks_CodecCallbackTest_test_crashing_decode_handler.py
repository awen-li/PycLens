# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_crashing_decode_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def forward_shorter_than_end(exc):
        if isinstance(exc, UnicodeDecodeError):
            return ('�', exc.start + 1)
        else:
            raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error('test.forward_shorter_than_end', forward_shorter_than_end)
    self.assertEqual(b'\xd8\xd8\xd8\xd8\xd8\x00\x00\x00'.decode('utf-16-le', 'test.forward_shorter_than_end'), '����Ø\x00')
    self.assertEqual(b'\xd8\xd8\xd8\xd8\x00\xd8\x00\x00'.decode('utf-16-be', 'test.forward_shorter_than_end'), '����Ø\x00')
    self.assertEqual(b'\x11\x11\x11\x11\x11\x00\x00\x00\x00\x00\x00'.decode('utf-32-le', 'test.forward_shorter_than_end'), '���ᄑ\x00')
    self.assertEqual(b'\x11\x11\x11\x00\x00\x11\x11\x00\x00\x00\x00'.decode('utf-32-be', 'test.forward_shorter_than_end'), '���ᄑ\x00')

    def replace_with_long(exc):
        if isinstance(exc, UnicodeDecodeError):
            exc.object = b'\x00' * 8
            return ('�', exc.start)
        else:
            raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error('test.replace_with_long', replace_with_long)
    self.assertEqual(b'\x00'.decode('utf-16', 'test.replace_with_long'), '�\x00\x00\x00\x00')
    self.assertEqual(b'\x00'.decode('utf-32', 'test.replace_with_long'), '�\x00\x00')
