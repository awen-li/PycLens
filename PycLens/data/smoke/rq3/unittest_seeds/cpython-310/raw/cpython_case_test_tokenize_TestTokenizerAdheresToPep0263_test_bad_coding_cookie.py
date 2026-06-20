# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestTokenizerAdheresToPep0263_test_bad_coding_cookie

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(SyntaxError, self._testFile, 'bad_coding.py')
    self.assertRaises(SyntaxError, self._testFile, 'bad_coding2.py')
