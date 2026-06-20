# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TokenizeTest_test_implicit_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = BytesIO('x'.encode('utf-8'))
    tokens = list(tokenize(f.readline))
    self.assertEqual(tokens[-2].type, NEWLINE)
    self.assertEqual(tokens[-1].type, ENDMARKER)
