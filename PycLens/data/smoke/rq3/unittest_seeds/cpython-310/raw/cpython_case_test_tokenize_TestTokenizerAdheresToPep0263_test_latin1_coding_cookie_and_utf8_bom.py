# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestTokenizerAdheresToPep0263_test_latin1_coding_cookie_and_utf8_bom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = 'tokenize_tests-latin1-coding-cookie-and-utf8-bom-sig.txt'
    self.assertRaises(SyntaxError, self._testFile, f)
