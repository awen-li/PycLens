# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ErrorReportingTest_test_expat_incomplete

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = create_parser()
    parser.setContentHandler(ContentHandler())
    self.assertRaises(SAXParseException, parser.parse, StringIO('<foo>'))
    self.assertEqual(parser.getColumnNumber(), 5)
    self.assertEqual(parser.getLineNumber(), 1)
