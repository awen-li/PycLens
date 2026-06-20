# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_xmlcharnamereplace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def xmlcharnamereplace(exc):
        if not isinstance(exc, UnicodeEncodeError):
            raise TypeError("don't know how to handle %r" % exc)
        l = []
        for c in exc.object[exc.start:exc.end]:
            try:
                l.append('&%s;' % html.entities.codepoint2name[ord(c)])
            except KeyError:
                l.append('&#%d;' % ord(c))
        return (''.join(l), exc.end)
    codecs.register_error('test.xmlcharnamereplace', xmlcharnamereplace)
    sin = '«ℜ» = 〈ሴ€〉'
    sout = b'&laquo;&real;&raquo; = &lang;&#4660;&euro;&rang;'
    self.assertEqual(sin.encode('ascii', 'test.xmlcharnamereplace'), sout)
    sout = b'\xab&real;\xbb = &lang;&#4660;&euro;&rang;'
    self.assertEqual(sin.encode('latin-1', 'test.xmlcharnamereplace'), sout)
    sout = b'\xab&real;\xbb = &lang;&#4660;\xa4&rang;'
    self.assertEqual(sin.encode('iso-8859-15', 'test.xmlcharnamereplace'), sout)
