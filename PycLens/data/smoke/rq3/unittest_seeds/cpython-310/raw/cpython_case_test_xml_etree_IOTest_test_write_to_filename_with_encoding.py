# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_write_to_filename_with_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, TESTFN)
    tree = ET.ElementTree(ET.XML('<site>ø</site>'))
    tree.write(TESTFN, encoding='utf-8')
    with open(TESTFN, 'rb') as f:
        self.assertEqual(f.read(), b'<site>\xc3\xb8</site>')
    tree.write(TESTFN, encoding='ISO-8859-1')
    with open(TESTFN, 'rb') as f:
        self.assertEqual(f.read(), convlinesep(b"<?xml version='1.0' encoding='ISO-8859-1'?>\n<site>\xf8</site>"))
