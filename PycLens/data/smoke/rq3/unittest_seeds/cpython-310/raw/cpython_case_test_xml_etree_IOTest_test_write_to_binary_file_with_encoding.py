# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_write_to_binary_file_with_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, TESTFN)
    tree = ET.ElementTree(ET.XML('<site>ø</site>'))
    with open(TESTFN, 'wb') as f:
        tree.write(f, encoding='utf-8')
        self.assertFalse(f.closed)
    with open(TESTFN, 'rb') as f:
        self.assertEqual(f.read(), b'<site>\xc3\xb8</site>')
    with open(TESTFN, 'wb') as f:
        tree.write(f, encoding='ISO-8859-1')
        self.assertFalse(f.closed)
    with open(TESTFN, 'rb') as f:
        self.assertEqual(f.read(), b"<?xml version='1.0' encoding='ISO-8859-1'?>\n<site>\xf8</site>")
