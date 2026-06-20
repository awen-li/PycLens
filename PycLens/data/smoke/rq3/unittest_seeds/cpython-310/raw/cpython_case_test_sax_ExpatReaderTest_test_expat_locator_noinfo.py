# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_locator_noinfo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = BytesIO()
    xmlgen = XMLGenerator(result)
    parser = create_parser()
    parser.setContentHandler(xmlgen)
    parser.feed('<doc>')
    parser.feed('</doc>')
    parser.close()
    self.assertEqual(parser.getSystemId(), None)
    self.assertEqual(parser.getPublicId(), None)
    self.assertEqual(parser.getLineNumber(), 1)
