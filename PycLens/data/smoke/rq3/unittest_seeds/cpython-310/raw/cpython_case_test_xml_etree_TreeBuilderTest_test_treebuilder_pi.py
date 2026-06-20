# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_treebuilder_pi

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = ET.TreeBuilder()
    self.assertEqual(b.pi('target', None).tag, ET.PI)
    self.assertEqual(b.pi('target', None).text, 'target')
    b = ET.TreeBuilder(pi_factory=ET.PI)
    self.assertEqual(b.pi('target').tag, ET.PI)
    self.assertEqual(b.pi('target').text, 'target')
    self.assertEqual(b.pi('pitarget', ' text ').tag, ET.PI)
    self.assertEqual(b.pi('pitarget', ' text ').text, 'pitarget  text ')
    b = ET.TreeBuilder(pi_factory=lambda target, text: (len(target), text))
    self.assertEqual(b.pi('target'), (len('target'), None))
    self.assertEqual(b.pi('pitarget', ' text '), (len('pitarget'), ' text '))
