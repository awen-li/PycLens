# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: ErrorReportingTest_test_sax_parse_exception_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    str(SAXParseException('message', None, self.DummyLocator(1, 1)))
    str(SAXParseException('message', None, self.DummyLocator(None, 1)))
    str(SAXParseException('message', None, self.DummyLocator(1, None)))
    str(SAXParseException('message', None, self.DummyLocator(None, None)))
