# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTypeTest_test_istype

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(ET.ParseError, type)
    self.assertIsInstance(ET.QName, type)
    self.assertIsInstance(ET.ElementTree, type)
    self.assertIsInstance(ET.Element, type)
    self.assertIsInstance(ET.TreeBuilder, type)
    self.assertIsInstance(ET.XMLParser, type)
