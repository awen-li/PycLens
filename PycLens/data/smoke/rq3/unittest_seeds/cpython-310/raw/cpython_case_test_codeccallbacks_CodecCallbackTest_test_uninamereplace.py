# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_uninamereplace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def uninamereplace(exc):
        if not isinstance(exc, UnicodeEncodeError):
            raise TypeError("don't know how to handle %r" % exc)
        l = []
        for c in exc.object[exc.start:exc.end]:
            l.append(unicodedata.name(c, '0x%x' % ord(c)))
        return ('\x1b[1m%s\x1b[0m' % ', '.join(l), exc.end)
    codecs.register_error('test.uninamereplace', uninamereplace)
    sin = '¬ሴ€耀'
    sout = b'\x1b[1mNOT SIGN, ETHIOPIC SYLLABLE SEE, EURO SIGN, CJK UNIFIED IDEOGRAPH-8000\x1b[0m'
    self.assertEqual(sin.encode('ascii', 'test.uninamereplace'), sout)
    sout = b'\xac\x1b[1mETHIOPIC SYLLABLE SEE, EURO SIGN, CJK UNIFIED IDEOGRAPH-8000\x1b[0m'
    self.assertEqual(sin.encode('latin-1', 'test.uninamereplace'), sout)
    sout = b'\xac\x1b[1mETHIOPIC SYLLABLE SEE\x1b[0m\xa4\x1b[1mCJK UNIFIED IDEOGRAPH-8000\x1b[0m'
    self.assertEqual(sin.encode('iso-8859-15', 'test.uninamereplace'), sout)
