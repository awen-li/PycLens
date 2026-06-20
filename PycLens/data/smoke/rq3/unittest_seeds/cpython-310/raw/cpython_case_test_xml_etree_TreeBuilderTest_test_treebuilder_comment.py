# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_treebuilder_comment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = ET.TreeBuilder()
    self.assertEqual(b.comment('ctext').tag, ET.Comment)
    self.assertEqual(b.comment('ctext').text, 'ctext')
    b = ET.TreeBuilder(comment_factory=ET.Comment)
    self.assertEqual(b.comment('ctext').tag, ET.Comment)
    self.assertEqual(b.comment('ctext').text, 'ctext')
    b = ET.TreeBuilder(comment_factory=len)
    self.assertEqual(b.comment('ctext'), len('ctext'))
