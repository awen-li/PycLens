# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_short_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    readline = self.get_readline((b'print(something)\n',))
    (encoding, consumed_lines) = detect_encoding(readline)
    self.assertEqual(encoding, 'utf-8')
    self.assertEqual(consumed_lines, [b'print(something)\n'])
    (encoding, consumed_lines) = detect_encoding(self.get_readline(()))
    self.assertEqual(encoding, 'utf-8')
    self.assertEqual(consumed_lines, [])
    readline = self.get_readline((b'\xef\xbb\xbfprint(something)\n',))
    (encoding, consumed_lines) = detect_encoding(readline)
    self.assertEqual(encoding, 'utf-8-sig')
    self.assertEqual(consumed_lines, [b'print(something)\n'])
    readline = self.get_readline((b'\xef\xbb\xbf',))
    (encoding, consumed_lines) = detect_encoding(readline)
    self.assertEqual(encoding, 'utf-8-sig')
    self.assertEqual(consumed_lines, [])
    readline = self.get_readline((b'# coding: bad\n',))
    self.assertRaises(SyntaxError, detect_encoding, readline)
