# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_tostring_default_namespace_different_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = ET.XML('<body xmlns="http://effbot.org/ns"><tag/></body>')
    self.assertEqual(ET.tostring(elem, encoding='unicode', default_namespace='foobar'), '<ns1:body xmlns="foobar" xmlns:ns1="http://effbot.org/ns"><ns1:tag /></ns1:body>')
