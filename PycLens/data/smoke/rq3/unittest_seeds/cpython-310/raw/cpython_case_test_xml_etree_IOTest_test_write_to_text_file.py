# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_write_to_text_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, TESTFN)
    tree = ET.ElementTree(ET.XML('<site>ø</site>'))
    with open(TESTFN, 'w', encoding='utf-8') as f:
        tree.write(f, encoding='unicode')
        self.assertFalse(f.closed)
    with open(TESTFN, 'rb') as f:
        self.assertEqual(f.read(), b'<site>\xc3\xb8</site>')
    with open(TESTFN, 'w', encoding='ascii', errors='xmlcharrefreplace') as f:
        tree.write(f, encoding='unicode')
        self.assertFalse(f.closed)
    with open(TESTFN, 'rb') as f:
        self.assertEqual(f.read(), b'<site>&#248;</site>')
    with open(TESTFN, 'w', encoding='ISO-8859-1') as f:
        tree.write(f, encoding='unicode')
        self.assertFalse(f.closed)
    with open(TESTFN, 'rb') as f:
        self.assertEqual(f.read(), b'<site>\xf8</site>')
