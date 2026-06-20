# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_decodehelper

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(LookupError, b'\xff'.decode, 'ascii', 'test.unknown')

    def baddecodereturn1(exc):
        return 42
    codecs.register_error('test.baddecodereturn1', baddecodereturn1)
    self.assertRaises(TypeError, b'\xff'.decode, 'ascii', 'test.baddecodereturn1')
    self.assertRaises(TypeError, b'\\'.decode, 'unicode-escape', 'test.baddecodereturn1')
    self.assertRaises(TypeError, b'\\x0'.decode, 'unicode-escape', 'test.baddecodereturn1')
    self.assertRaises(TypeError, b'\\x0y'.decode, 'unicode-escape', 'test.baddecodereturn1')
    self.assertRaises(TypeError, b'\\Uffffeeee'.decode, 'unicode-escape', 'test.baddecodereturn1')
    self.assertRaises(TypeError, b'\\uyyyy'.decode, 'raw-unicode-escape', 'test.baddecodereturn1')

    def baddecodereturn2(exc):
        return ('?', None)
    codecs.register_error('test.baddecodereturn2', baddecodereturn2)
    self.assertRaises(TypeError, b'\xff'.decode, 'ascii', 'test.baddecodereturn2')
    handler = PosReturn()
    codecs.register_error('test.posreturn', handler.handle)
    handler.pos = -1
    self.assertEqual(b'\xff0'.decode('ascii', 'test.posreturn'), '<?>0')
    handler.pos = -2
    self.assertEqual(b'\xff0'.decode('ascii', 'test.posreturn'), '<?><?>')
    handler.pos = -3
    self.assertRaises(IndexError, b'\xff0'.decode, 'ascii', 'test.posreturn')
    handler.pos = 1
    self.assertEqual(b'\xff0'.decode('ascii', 'test.posreturn'), '<?>0')
    handler.pos = 2
    self.assertEqual(b'\xff0'.decode('ascii', 'test.posreturn'), '<?>')
    handler.pos = 3
    self.assertRaises(IndexError, b'\xff0'.decode, 'ascii', 'test.posreturn')
    handler.pos = 6
    self.assertEqual(b'\\uyyyy0'.decode('raw-unicode-escape', 'test.posreturn'), '<?>0')

    class D(dict):

        def __getitem__(self, key):
            raise ValueError
    self.assertRaises(UnicodeError, codecs.charmap_decode, b'\xff', 'strict', {255: None})
    self.assertRaises(ValueError, codecs.charmap_decode, b'\xff', 'strict', D())
    self.assertRaises(TypeError, codecs.charmap_decode, b'\xff', 'strict', {255: sys.maxunicode + 1})
