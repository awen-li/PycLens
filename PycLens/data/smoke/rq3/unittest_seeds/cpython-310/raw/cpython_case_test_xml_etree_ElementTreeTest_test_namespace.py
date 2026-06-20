# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML("<tag xml:lang='en' />")
    self.serialize_check(elem, '<tag xml:lang="en" />')
    elem = ET.XML("<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#' />")
    self.serialize_check(elem, '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" />')
    elem = ET.XML("<html:html xmlns:html='http://www.w3.org/1999/xhtml' />")
    self.serialize_check(elem, '<html:html xmlns:html="http://www.w3.org/1999/xhtml" />')
    elem = ET.XML("<soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope' />")
    self.serialize_check(elem, '<ns0:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope" />')
    elem = ET.XML(SAMPLE_XML_NS)
    self.serialize_check(elem, '<ns0:body xmlns:ns0="http://effbot.org/ns">\n  <ns0:tag>text</ns0:tag>\n  <ns0:tag />\n  <ns0:section>\n    <ns0:tag>subtext</ns0:tag>\n  </ns0:section>\n</ns0:body>')
