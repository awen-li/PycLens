# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_cookie_second_line_empty_first_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = (b'\n', b'# vim: set fileencoding=iso8859-15 :\n', b"print('\xe2\x82\xac')\n")
    (encoding, consumed_lines) = detect_encoding(self.get_readline(lines))
    self.assertEqual(encoding, 'iso8859-15')
    expected = [b'\n', b'# vim: set fileencoding=iso8859-15 :\n']
    self.assertEqual(consumed_lines, expected)
