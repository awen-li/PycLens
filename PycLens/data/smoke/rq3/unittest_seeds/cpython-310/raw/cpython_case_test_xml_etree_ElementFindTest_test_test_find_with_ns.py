# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementFindTest_test_test_find_with_ns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.XML(SAMPLE_XML_NS)
    self.assertEqual(summarize_list(e.findall('tag')), [])
    self.assertEqual(summarize_list(e.findall('{http://effbot.org/ns}tag')), ['{http://effbot.org/ns}tag'] * 2)
    self.assertEqual(summarize_list(e.findall('.//{http://effbot.org/ns}tag')), ['{http://effbot.org/ns}tag'] * 3)
