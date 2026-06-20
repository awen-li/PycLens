# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_xmlgen_content_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.ioclass()
    gen = XMLGenerator(result)
    gen.startDocument()
    gen.startElement('doc', {})
    gen.characters('<huhei&')
    gen.endElement('doc')
    gen.endDocument()
    self.assertEqual(result.getvalue(), self.xml('<doc>&lt;huhei&amp;</doc>'))
