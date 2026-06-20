# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_backslashescape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sin = 'a¬ሴ€耀\U0010ffff'
    sout = b'a\\xac\\u1234\\u20ac\\u8000\\U0010ffff'
    self.assertEqual(sin.encode('ascii', 'backslashreplace'), sout)
    sout = b'a\xac\\u1234\\u20ac\\u8000\\U0010ffff'
    self.assertEqual(sin.encode('latin-1', 'backslashreplace'), sout)
    sout = b'a\xac\\u1234\xa4\\u8000\\U0010ffff'
    self.assertEqual(sin.encode('iso-8859-15', 'backslashreplace'), sout)
