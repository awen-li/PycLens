# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_treebuilder_elementfactory_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ET.XMLParser(target=ET.TreeBuilder(element_factory=None))
    parser.feed(self.sample1)
    e = parser.close()
    self._check_sample1_element(e)
