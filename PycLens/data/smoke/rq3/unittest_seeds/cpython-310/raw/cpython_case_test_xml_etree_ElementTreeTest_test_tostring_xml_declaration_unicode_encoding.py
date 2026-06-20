# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_tostring_xml_declaration_unicode_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<body><tag/></body>')
    self.assertEqual(ET.tostring(elem, encoding='unicode', xml_declaration=True), "<?xml version='1.0' encoding='utf-8'?>\n<body><tag /></body>")
