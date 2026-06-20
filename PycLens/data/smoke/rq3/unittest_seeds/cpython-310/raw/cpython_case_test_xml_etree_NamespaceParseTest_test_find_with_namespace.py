# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: NamespaceParseTest_test_find_with_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nsmap = {'h': 'hello', 'f': 'foo'}
    doc = ET.fromstring(SAMPLE_XML_NS_ELEMS)
    self.assertEqual(len(doc.findall('{hello}table', nsmap)), 1)
    self.assertEqual(len(doc.findall('.//{hello}td', nsmap)), 2)
    self.assertEqual(len(doc.findall('.//{foo}name', nsmap)), 1)
