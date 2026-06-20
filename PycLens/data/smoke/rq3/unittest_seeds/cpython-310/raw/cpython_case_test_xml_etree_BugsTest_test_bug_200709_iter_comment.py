# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_200709_iter_comment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = ET.Element('a')
    b = ET.SubElement(a, 'b')
    comment_b = ET.Comment('TEST-b')
    b.append(comment_b)
    self.assertEqual(summarize_list(a.iter(ET.Comment)), [ET.Comment])
