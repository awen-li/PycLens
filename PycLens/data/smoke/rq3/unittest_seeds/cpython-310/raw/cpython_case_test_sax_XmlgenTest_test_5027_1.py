# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_5027_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_xml = StringIO('<?xml version="1.0"?><a:g1 xmlns:a="http://example.com/ns"><a:g2 xml:lang="en">Hello</a:g2></a:g1>')
    parser = make_parser()
    parser.setFeature(feature_namespaces, True)
    result = self.ioclass()
    gen = XMLGenerator(result)
    parser.setContentHandler(gen)
    parser.parse(test_xml)
    self.assertEqual(result.getvalue(), self.xml('<a:g1 xmlns:a="http://example.com/ns"><a:g2 xml:lang="en">Hello</a:g2></a:g1>'))
