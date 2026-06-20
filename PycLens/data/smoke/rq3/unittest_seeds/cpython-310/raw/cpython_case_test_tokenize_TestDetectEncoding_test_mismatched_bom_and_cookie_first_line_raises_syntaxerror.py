# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_mismatched_bom_and_cookie_first_line_raises_syntaxerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = (b'\xef\xbb\xbf# vim: set fileencoding=ascii :\n', b'print(something)\n', b'do_something(else)\n')
    readline = self.get_readline(lines)
    self.assertRaises(SyntaxError, detect_encoding, readline)
