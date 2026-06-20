# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_element_factory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lst = []

    def myfactory(tag, attrib):
        nonlocal lst
        lst.append(tag)
        return ET.Element(tag, attrib)
    tb = ET.TreeBuilder(element_factory=myfactory)
    parser = ET.XMLParser(target=tb)
    parser.feed(self.sample2)
    parser.close()
    self.assertEqual(lst, ['toplevel'])
