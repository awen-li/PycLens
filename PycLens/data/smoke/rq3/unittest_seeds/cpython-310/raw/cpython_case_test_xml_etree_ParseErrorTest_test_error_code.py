# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ParseErrorTest_test_error_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import xml.parsers.expat.errors as ERRORS
    self.assertEqual(self._get_error('foo').code, ERRORS.codes[ERRORS.XML_ERROR_SYNTAX])
