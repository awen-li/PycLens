# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_initialize_parser_without_target

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ET.XMLParser(target=None)
    self.assertIsInstance(parser.target, ET.TreeBuilder)
    parser2 = ET.XMLParser()
    self.assertIsInstance(parser2.target, ET.TreeBuilder)
