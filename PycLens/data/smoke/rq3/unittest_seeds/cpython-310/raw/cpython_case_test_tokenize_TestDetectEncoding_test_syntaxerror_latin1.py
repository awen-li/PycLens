# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_syntaxerror_latin1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = (b'print("\xdf")',)
    readline = self.get_readline(lines)
    self.assertRaises(SyntaxError, detect_encoding, readline)
