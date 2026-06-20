# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_tostringlist_invariant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = ET.fromstring('<tag>foo</tag>')
    self.assertEqual(ET.tostring(root, 'unicode'), ''.join(ET.tostringlist(root, 'unicode')))
    self.assertEqual(ET.tostring(root, 'utf-16'), b''.join(ET.tostringlist(root, 'utf-16')))
