# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_file_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stringfile = io.BytesIO(SAMPLE_XML.encode('utf-8'))
    tree = ET.ElementTree(file=stringfile)
    self.assertEqual(tree.find('tag').tag, 'tag')
    self.assertEqual(tree.find('section/tag').tag, 'tag')
    tree = ET.ElementTree(file=SIMPLE_XMLFILE)
    self.assertEqual(tree.find('element').tag, 'element')
    self.assertEqual(tree.find('element/../empty-element').tag, 'empty-element')
