# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_read_from_user_binary_reader

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = io.BytesIO(b'<?xml version="1.0"?><site></site>')
    reader = self.dummy()
    reader.read = raw.read
    tree = ET.ElementTree()
    tree.parse(reader)
    self.assertEqual(tree.getroot().tag, 'site')
    tree = ET.ElementTree()
