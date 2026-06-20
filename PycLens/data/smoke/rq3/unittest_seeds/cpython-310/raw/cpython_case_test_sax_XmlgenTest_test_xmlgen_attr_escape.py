# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_xmlgen_attr_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.ioclass()
    gen = XMLGenerator(result)
    gen.startDocument()
    gen.startElement('doc', {'a': '"'})
    gen.startElement('e', {'a': "'"})
    gen.endElement('e')
    gen.startElement('e', {'a': '\'"'})
    gen.endElement('e')
    gen.startElement('e', {'a': '\n\r\t'})
    gen.endElement('e')
    gen.endElement('doc')
    gen.endDocument()
    self.assertEqual(result.getvalue(), self.xml('<doc a=\'"\'><e a="\'"></e><e a="\'&quot;"></e><e a="&#10;&#13;&#9;"></e></doc>'))
