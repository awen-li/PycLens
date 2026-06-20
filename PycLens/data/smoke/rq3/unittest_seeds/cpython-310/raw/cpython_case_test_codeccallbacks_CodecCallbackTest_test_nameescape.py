# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_nameescape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sin = 'a¬ሴ€耀\U0010ffff'
    sout = b'a\\N{NOT SIGN}\\N{ETHIOPIC SYLLABLE SEE}\\N{EURO SIGN}\\N{CJK UNIFIED IDEOGRAPH-8000}\\U0010ffff'
    self.assertEqual(sin.encode('ascii', 'namereplace'), sout)
    sout = b'a\xac\\N{ETHIOPIC SYLLABLE SEE}\\N{EURO SIGN}\\N{CJK UNIFIED IDEOGRAPH-8000}\\U0010ffff'
    self.assertEqual(sin.encode('latin-1', 'namereplace'), sout)
    sout = b'a\xac\\N{ETHIOPIC SYLLABLE SEE}\xa4\\N{CJK UNIFIED IDEOGRAPH-8000}\\U0010ffff'
    self.assertEqual(sin.encode('iso-8859-15', 'namereplace'), sout)
