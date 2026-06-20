# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_xmlgen_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodings = ('iso-8859-15', 'utf-8', 'utf-8-sig', 'utf-16', 'utf-16be', 'utf-16le', 'utf-32', 'utf-32be', 'utf-32le')
    for encoding in encodings:
        result = self.ioclass()
        gen = XMLGenerator(result, encoding=encoding)
        gen.startDocument()
        gen.startElement('doc', {'a': '€'})
        gen.characters('€')
        gen.endElement('doc')
        gen.endDocument()
        self.assertEqual(result.getvalue(), self.xml('<doc a="€">€</doc>', encoding=encoding))
