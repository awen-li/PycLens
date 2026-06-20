# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_200709_register_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.Element('{http://namespace.invalid/does/not/exist/}title')
    self.assertEqual(ET.tostring(e), b'<ns0:title xmlns:ns0="http://namespace.invalid/does/not/exist/" />')
    ET.register_namespace('foo', 'http://namespace.invalid/does/not/exist/')
    e = ET.Element('{http://namespace.invalid/does/not/exist/}title')
    self.assertEqual(ET.tostring(e), b'<foo:title xmlns:foo="http://namespace.invalid/does/not/exist/" />')
    e = ET.Element('{http://purl.org/dc/elements/1.1/}title')
    self.assertEqual(ET.tostring(e), b'<dc:title xmlns:dc="http://purl.org/dc/elements/1.1/" />')
