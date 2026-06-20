# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_encode_unencodable_replacement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def unencrepl(exc):
        if isinstance(exc, UnicodeEncodeError):
            return (repl, exc.end)
        else:
            raise TypeError("don't know how to handle %r" % exc)
    codecs.register_error('test.unencreplhandler', unencrepl)
    for (enc, input, repl) in (('ascii', '[¤]', '½'), ('iso-8859-1', '[€]', 'œ'), ('iso-8859-15', '[¤]', '½'), ('utf-8', '[\udc80]', '\udcff'), ('utf-16', '[\udc80]', '\udcff'), ('utf-32', '[\udc80]', '\udcff')):
        with self.subTest(encoding=enc):
            with self.assertRaises(UnicodeEncodeError) as cm:
                input.encode(enc, 'test.unencreplhandler')
            exc = cm.exception
            self.assertEqual(exc.start, 1)
            self.assertEqual(exc.end, 2)
            self.assertEqual(exc.object, input)
