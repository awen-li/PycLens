# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_write_to_binary_file_with_bom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, TESTFN)
    tree = ET.ElementTree(ET.XML('<site>ø</site>'))
    with open(TESTFN, 'wb') as f:
        tree.write(f, encoding='utf-16')
        self.assertFalse(f.closed)
    with open(TESTFN, 'rb') as f:
        self.assertEqual(f.read(), "<?xml version='1.0' encoding='utf-16'?>\n<site>ø</site>".encode('utf-16'))
    with open(TESTFN, 'wb', buffering=0) as f:
        tree.write(f, encoding='utf-16')
        self.assertFalse(f.closed)
    with open(TESTFN, 'rb') as f:
        self.assertEqual(f.read(), "<?xml version='1.0' encoding='utf-16'?>\n<site>ø</site>".encode('utf-16'))
