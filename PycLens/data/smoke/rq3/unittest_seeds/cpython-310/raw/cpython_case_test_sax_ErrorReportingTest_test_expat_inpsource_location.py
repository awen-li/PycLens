# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ErrorReportingTest_test_expat_inpsource_location

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = create_parser()
    parser.setContentHandler(ContentHandler())
    source = InputSource()
    source.setByteStream(BytesIO(b'<foo bar foobar>'))
    name = 'a file name'
    source.setSystemId(name)
    try:
        parser.parse(source)
        self.fail()
    except SAXException as e:
        self.assertEqual(e.getSystemId(), name)
