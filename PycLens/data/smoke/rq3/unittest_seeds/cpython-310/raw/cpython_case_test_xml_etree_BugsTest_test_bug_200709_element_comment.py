# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_200709_element_comment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = ET.Element('a')
    a.append(ET.Comment('foo'))
    self.assertEqual(a[0].tag, ET.Comment)
    a = ET.Element('a')
    a.append(ET.PI('foo'))
    self.assertEqual(a[0].tag, ET.PI)
