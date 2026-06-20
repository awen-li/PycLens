# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLParserTest_test_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyParser(ET.XMLParser):
        pass
    parser = MyParser()
    parser.feed(self.sample1)
    self._check_sample_element(parser.close())
