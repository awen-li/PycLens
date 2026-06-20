# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_writestring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<html><body>text</body></html>')
    self.assertEqual(ET.tostring(elem), b'<html><body>text</body></html>')
    elem = ET.fromstring('<html><body>text</body></html>')
    self.assertEqual(ET.tostring(elem), b'<html><body>text</body></html>')
