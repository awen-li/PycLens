# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_tree_write_attribute_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = ET.Element('cirriculum', status='public', company='example')
    self.assertEqual(serialize(root), '<cirriculum status="public" company="example" />')
    self.assertEqual(serialize(root, method='html'), '<cirriculum status="public" company="example"></cirriculum>')
