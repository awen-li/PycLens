# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_mutatingdecodehandler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    baddata = [('ascii', b'\xff'), ('utf-7', b'++'), ('utf-8', b'\xff'), ('utf-16', b'\xff'), ('utf-32', b'\xff'), ('unicode-escape', b'\\u123g'), ('raw-unicode-escape', b'\\u123g')]

    def replacing(exc):
        if isinstance(exc, UnicodeDecodeError):
            exc.object = 42
            return ('䉂', 0)
        else:
            raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error('test.replacing', replacing)
    for (encoding, data) in baddata:
        with self.assertRaises(TypeError):
            data.decode(encoding, 'test.replacing')

    def mutating(exc):
        if isinstance(exc, UnicodeDecodeError):
            exc.object = b''
            return ('䉂', 0)
        else:
            raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error('test.mutating', mutating)
    for (encoding, data) in baddata:
        self.assertEqual(data.decode(encoding, 'test.mutating'), '䉂')
