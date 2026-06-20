# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_attlist_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = ET.fromstring(ATTLIST_XML)
    self.assertEqual(root[0].attrib, {'{http://www.w3.org/XML/1998/namespace}lang': 'eng'})
