# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_xmltoolkit28

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ET.XML('<doc><table><tbody/></table></doc>')
    self.assertEqual(summarize_list(tree.findall('.//thead')), [])
    self.assertEqual(summarize_list(tree.findall('.//tbody')), ['tbody'])
