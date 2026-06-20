# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_false_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    readline = self.get_readline((b'print("#coding=fake")',))
    (encoding, consumed_lines) = detect_encoding(readline)
    self.assertEqual(encoding, 'utf-8')
    self.assertEqual(consumed_lines, [b'print("#coding=fake")'])
