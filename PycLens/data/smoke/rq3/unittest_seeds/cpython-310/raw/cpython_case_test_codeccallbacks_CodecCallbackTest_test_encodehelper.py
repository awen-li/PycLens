# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_encodehelper

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(LookupError, 'ÿ'.encode, 'ascii', 'test.unknown')

    def badencodereturn1(exc):
        return 42
    codecs.register_error('test.badencodereturn1', badencodereturn1)
    self.assertRaises(TypeError, 'ÿ'.encode, 'ascii', 'test.badencodereturn1')

    def badencodereturn2(exc):
        return ('?', None)
    codecs.register_error('test.badencodereturn2', badencodereturn2)
    self.assertRaises(TypeError, 'ÿ'.encode, 'ascii', 'test.badencodereturn2')
    handler = PosReturn()
    codecs.register_error('test.posreturn', handler.handle)
    handler.pos = -1
    self.assertEqual('ÿ0'.encode('ascii', 'test.posreturn'), b'<?>0')
    handler.pos = -2
    self.assertEqual('ÿ0'.encode('ascii', 'test.posreturn'), b'<?><?>')
    handler.pos = -3
    self.assertRaises(IndexError, 'ÿ0'.encode, 'ascii', 'test.posreturn')
    handler.pos = 1
    self.assertEqual('ÿ0'.encode('ascii', 'test.posreturn'), b'<?>0')
    handler.pos = 2
    self.assertEqual('ÿ0'.encode('ascii', 'test.posreturn'), b'<?>')
    handler.pos = 3
    self.assertRaises(IndexError, 'ÿ0'.encode, 'ascii', 'test.posreturn')
    handler.pos = 0

    class D(dict):

        def __getitem__(self, key):
            raise ValueError
    for err in ('strict', 'replace', 'xmlcharrefreplace', 'backslashreplace', 'namereplace', 'test.posreturn'):
        self.assertRaises(UnicodeError, codecs.charmap_encode, 'ÿ', err, {255: None})
        self.assertRaises(ValueError, codecs.charmap_encode, 'ÿ', err, D())
        self.assertRaises(TypeError, codecs.charmap_encode, 'ÿ', err, {255: 300})
