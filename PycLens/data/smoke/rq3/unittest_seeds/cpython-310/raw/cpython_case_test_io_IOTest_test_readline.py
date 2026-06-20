# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_readline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, 'wb') as f:
        f.write(b'abc\ndef\nxyzzy\nfoo\x00bar\nanother line')
    with self.open(os_helper.TESTFN, 'rb') as f:
        self.assertEqual(f.readline(), b'abc\n')
        self.assertEqual(f.readline(10), b'def\n')
        self.assertEqual(f.readline(2), b'xy')
        self.assertEqual(f.readline(4), b'zzy\n')
        self.assertEqual(f.readline(), b'foo\x00bar\n')
        self.assertEqual(f.readline(None), b'another line')
        self.assertRaises(TypeError, f.readline, 5.3)
    with self.open(os_helper.TESTFN, 'r', encoding='utf-8') as f:
        self.assertRaises(TypeError, f.readline, 5.3)
