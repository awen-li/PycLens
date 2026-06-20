# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_xmltoolkit54

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.XML("<!DOCTYPE doc [<!ENTITY ldots '&#x8230;'>]><doc>&ldots;</doc>")
    self.assertEqual(serialize(e, encoding='us-ascii'), b'<doc>&#33328;</doc>')
    self.assertEqual(serialize(e), '<doc>舰</doc>')
