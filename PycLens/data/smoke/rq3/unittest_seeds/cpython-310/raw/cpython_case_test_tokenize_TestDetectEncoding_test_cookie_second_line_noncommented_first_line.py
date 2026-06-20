# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_cookie_second_line_noncommented_first_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = (b"print('\xc2\xa3')\n", b'# vim: set fileencoding=iso8859-15 :\n', b"print('\xe2\x82\xac')\n")
    (encoding, consumed_lines) = detect_encoding(self.get_readline(lines))
    self.assertEqual(encoding, 'utf-8')
    expected = [b"print('\xc2\xa3')\n"]
    self.assertEqual(consumed_lines, expected)
