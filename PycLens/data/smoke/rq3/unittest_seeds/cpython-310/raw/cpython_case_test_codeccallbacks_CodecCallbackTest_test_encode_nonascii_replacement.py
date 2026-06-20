# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_encode_nonascii_replacement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def handle(exc):
        if isinstance(exc, UnicodeEncodeError):
            return (repl, exc.end)
        raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error('test.replacing', handle)
    for (enc, input, repl) in (('ascii', '[¤]', 'abc'), ('iso-8859-1', '[€]', '½¾'), ('iso-8859-15', '[¤]', 'œŸ')):
        res = input.encode(enc, 'test.replacing')
        self.assertEqual(res, ('[' + repl + ']').encode(enc))
    for (enc, input, repl) in (('utf-8', '[\udc80]', '🐍'), ('utf-16', '[\udc80]', '🐍'), ('utf-32', '[\udc80]', '🐍')):
        with self.subTest(encoding=enc):
            with self.assertRaises(UnicodeEncodeError) as cm:
                input.encode(enc, 'test.replacing')
            exc = cm.exception
            self.assertEqual(exc.start, 1)
            self.assertEqual(exc.end, 2)
            self.assertEqual(exc.object, input)
