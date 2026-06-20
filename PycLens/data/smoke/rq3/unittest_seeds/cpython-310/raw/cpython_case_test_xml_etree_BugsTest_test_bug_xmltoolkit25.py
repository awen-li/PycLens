# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_xmltoolkit25

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML(SAMPLE_XML)
    tree = ET.ElementTree(elem)
    self.assertEqual(tree.findtext('tag'), 'text')
    self.assertEqual(tree.findtext('section/tag'), 'subtext')
