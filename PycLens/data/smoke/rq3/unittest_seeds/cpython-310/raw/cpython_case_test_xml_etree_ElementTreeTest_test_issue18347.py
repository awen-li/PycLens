# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_issue18347

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.XML('<html><CamelCase>text</CamelCase></html>')
    self.assertEqual(serialize(e), '<html><CamelCase>text</CamelCase></html>')
    self.assertEqual(serialize(e, method='html'), '<html><CamelCase>text</CamelCase></html>')
