# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_short_empty_elements

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = ET.fromstring('<tag>a<x />b<y></y>c</tag>')
    self.assertEqual(ET.tostring(root, 'unicode'), '<tag>a<x />b<y />c</tag>')
    self.assertEqual(ET.tostring(root, 'unicode', short_empty_elements=True), '<tag>a<x />b<y />c</tag>')
    self.assertEqual(ET.tostring(root, 'unicode', short_empty_elements=False), '<tag>a<x></x>b<y></y>c</tag>')
