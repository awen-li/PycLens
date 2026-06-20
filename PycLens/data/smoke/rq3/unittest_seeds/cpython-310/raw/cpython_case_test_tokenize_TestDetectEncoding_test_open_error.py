# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_open_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = BytesIO(b'#coding:xxx')
    with mock.patch('tokenize._builtin_open', return_value=m):
        self.assertRaises(SyntaxError, tokenize_open, 'foobar')
    self.assertTrue(m.closed)
