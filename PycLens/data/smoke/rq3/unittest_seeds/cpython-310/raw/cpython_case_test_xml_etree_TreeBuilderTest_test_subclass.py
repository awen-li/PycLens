# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyTreeBuilder(ET.TreeBuilder):

        def foobar(self, x):
            return x * 2
    tb = MyTreeBuilder()
    self.assertEqual(tb.foobar(10), 20)
    parser = ET.XMLParser(target=tb)
    parser.feed(self.sample1)
    e = parser.close()
    self._check_sample1_element(e)
