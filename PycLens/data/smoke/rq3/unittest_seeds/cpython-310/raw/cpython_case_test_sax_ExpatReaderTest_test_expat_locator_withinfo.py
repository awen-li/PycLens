# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ExpatReaderTest_test_expat_locator_withinfo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = BytesIO()
    xmlgen = XMLGenerator(result)
    parser = create_parser()
    parser.setContentHandler(xmlgen)
    parser.parse(TEST_XMLFILE)
    self.assertEqual(parser.getSystemId(), TEST_XMLFILE)
    self.assertEqual(parser.getPublicId(), None)
