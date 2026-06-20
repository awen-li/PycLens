# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_matched_bom_and_cookie_second_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = (b'\xef\xbb\xbf#! something\n', b'f# coding=utf-8\n', b'print(something)\n', b'do_something(else)\n')
    (encoding, consumed_lines) = detect_encoding(self.get_readline(lines))
    self.assertEqual(encoding, 'utf-8-sig')
    self.assertEqual(consumed_lines, [b'#! something\n', b'f# coding=utf-8\n'])
