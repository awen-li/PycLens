# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_read_from_stringio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ET.ElementTree()
    stream = io.StringIO('<?xml version="1.0"?><site></site>')
    tree.parse(stream)
    self.assertEqual(tree.getroot().tag, 'site')
