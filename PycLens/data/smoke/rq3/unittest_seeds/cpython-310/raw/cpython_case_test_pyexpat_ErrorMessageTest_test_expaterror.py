# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: ErrorMessageTest_test_expaterror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xml = b'<'
    parser = expat.ParserCreate()
    try:
        parser.Parse(xml, True)
        self.fail()
    except expat.ExpatError as e:
        self.assertEqual(e.code, errors.codes[errors.XML_ERROR_UNCLOSED_TOKEN])
