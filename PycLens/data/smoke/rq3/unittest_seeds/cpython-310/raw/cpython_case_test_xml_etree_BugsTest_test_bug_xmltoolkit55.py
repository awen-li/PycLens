# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_xmltoolkit55

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ET.ParseError) as cm:
        ET.XML(b"<!DOCTYPE doc SYSTEM 'doc.dtd'><doc>&ldots;&ndots;&rdots;</doc>")
    self.assertEqual(str(cm.exception), 'undefined entity &ldots;: line 1, column 36')
