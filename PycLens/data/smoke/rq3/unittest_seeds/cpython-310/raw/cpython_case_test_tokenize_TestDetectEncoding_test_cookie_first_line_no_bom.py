# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_cookie_first_line_no_bom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = (b'# -*- coding: latin-1 -*-\n', b'print(something)\n', b'do_something(else)\n')
    (encoding, consumed_lines) = detect_encoding(self.get_readline(lines))
    self.assertEqual(encoding, 'iso-8859-1')
    self.assertEqual(consumed_lines, [b'# -*- coding: latin-1 -*-\n'])
