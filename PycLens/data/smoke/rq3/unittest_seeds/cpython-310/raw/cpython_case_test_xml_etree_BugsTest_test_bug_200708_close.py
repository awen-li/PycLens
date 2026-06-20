# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BugsTest_test_bug_200708_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ET.XMLParser()
    parser.feed('<element>some text</element>')
    self.assertEqual(parser.close().tag, 'element')

    class EchoTarget:

        def close(self):
            return ET.Element('element')
    parser = ET.XMLParser(target=EchoTarget())
    parser.feed('<element>some text</element>')
    self.assertEqual(parser.close().tag, 'element')
