# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(codecs.strict_errors, codecs.lookup_error('strict'))
    self.assertEqual(codecs.ignore_errors, codecs.lookup_error('ignore'))
    self.assertEqual(codecs.strict_errors, codecs.lookup_error('strict'))
    self.assertEqual(codecs.xmlcharrefreplace_errors, codecs.lookup_error('xmlcharrefreplace'))
    self.assertEqual(codecs.backslashreplace_errors, codecs.lookup_error('backslashreplace'))
    self.assertEqual(codecs.namereplace_errors, codecs.lookup_error('namereplace'))
