# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_encode_odd_bytes_replacement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def handle(exc):
        if isinstance(exc, UnicodeEncodeError):
            return (repl, exc.end)
        raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error('test.replacing', handle)
    input = '[\udc80]'
    for (enc, repl) in (*itertools.product(('utf-16le', 'utf-16be'), [b'a', b'abc']), *itertools.product(('utf-32le', 'utf-32be'), [b'a', b'ab', b'abc', b'abcde'])):
        with self.subTest(encoding=enc, repl=repl):
            with self.assertRaises(UnicodeEncodeError) as cm:
                input.encode(enc, 'test.replacing')
            exc = cm.exception
            self.assertEqual(exc.start, 1)
            self.assertEqual(exc.end, 2)
            self.assertEqual(exc.object, input)
            self.assertEqual(exc.reason, 'surrogates not allowed')
