# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_200709_element_insert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = ET.Element('a')
    b = ET.SubElement(a, 'b')
    c = ET.SubElement(a, 'c')
    d = ET.Element('d')
    a.insert(0, d)
    self.assertEqual(summarize_list(a), ['d', 'b', 'c'])
    a.insert(-1, d)
    self.assertEqual(summarize_list(a), ['d', 'b', 'd', 'c'])
