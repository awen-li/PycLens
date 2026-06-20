# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_no_bom_no_encoding_cookie

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = (b'# something\n', b'print(something)\n', b'do_something(else)\n')
    (encoding, consumed_lines) = detect_encoding(self.get_readline(lines))
    self.assertEqual(encoding, 'utf-8')
    self.assertEqual(consumed_lines, list(lines[:2]))
