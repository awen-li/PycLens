# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_xmlgen_ns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.ioclass()
    gen = XMLGenerator(result)
    gen.startDocument()
    gen.startPrefixMapping('ns1', ns_uri)
    gen.startElementNS((ns_uri, 'doc'), 'ns1:doc', {})
    gen.startElementNS((None, 'udoc'), None, {})
    gen.endElementNS((None, 'udoc'), None)
    gen.endElementNS((ns_uri, 'doc'), 'ns1:doc')
    gen.endPrefixMapping('ns1')
    gen.endDocument()
    self.assertEqual(result.getvalue(), self.xml('<ns1:doc xmlns:ns1="%s"><udoc></udoc></ns1:doc>' % ns_uri))
