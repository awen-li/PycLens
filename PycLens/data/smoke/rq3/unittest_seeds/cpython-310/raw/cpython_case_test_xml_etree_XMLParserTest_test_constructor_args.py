# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLParserTest_test_constructor_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser2 = ET.XMLParser(encoding='utf-8', target=ET.TreeBuilder())
    parser2.feed(self.sample1)
    self._check_sample_element(parser2.close())
