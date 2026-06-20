# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodePageTest_test_incremental

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decoded = codecs.code_page_decode(932, b'\x82', 'strict', False)
    self.assertEqual(decoded, ('', 0))
    decoded = codecs.code_page_decode(932, b'\xe9\x80\xe9', 'strict', False)
    self.assertEqual(decoded, ('騾', 2))
    decoded = codecs.code_page_decode(932, b'\xe9\x80\xe9\x80', 'strict', False)
    self.assertEqual(decoded, ('騾騾', 4))
    decoded = codecs.code_page_decode(932, b'abc', 'strict', False)
    self.assertEqual(decoded, ('abc', 3))
