# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_449000

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.sub('\\r\\n', '\\n', 'abc\r\ndef\r\n'), 'abc\ndef\n')
    self.assertEqual(re.sub('\r\n', '\\n', 'abc\r\ndef\r\n'), 'abc\ndef\n')
    self.assertEqual(re.sub('\\r\\n', '\n', 'abc\r\ndef\r\n'), 'abc\ndef\n')
    self.assertEqual(re.sub('\r\n', '\n', 'abc\r\ndef\r\n'), 'abc\ndef\n')
