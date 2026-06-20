# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_dummy_builder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BaseDummyBuilder:

        def close(self):
            return 42

    class DummyBuilder(BaseDummyBuilder):
        data = start = end = lambda *a: None
    parser = ET.XMLParser(target=DummyBuilder())
    parser.feed(self.sample1)
    self.assertEqual(parser.close(), 42)
    parser = ET.XMLParser(target=BaseDummyBuilder())
    parser.feed(self.sample1)
    self.assertEqual(parser.close(), 42)
    parser = ET.XMLParser(target=object())
    parser.feed(self.sample1)
    self.assertIsNone(parser.close())
