# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_text_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = tempfile.SpooledTemporaryFile(mode='w+', max_size=10, encoding='utf-8')
    f.write('abc\n')
    f.seek(0)
    self.assertEqual(f.read(), 'abc\n')
    f.write('def\n')
    f.seek(0)
    self.assertEqual(f.read(), 'abc\ndef\n')
    self.assertFalse(f._rolled)
    self.assertEqual(f.mode, 'w+')
    self.assertIsNone(f.name)
    self.assertEqual(f.newlines, os.linesep)
    self.assertEqual(f.encoding, 'utf-8')
    self.assertEqual(f.errors, 'strict')
    f.write('xyzzy\n')
    f.seek(0)
    self.assertEqual(f.read(), 'abc\ndef\nxyzzy\n')
    f.write('foo\x1abar\n')
    f.seek(0)
    self.assertEqual(f.read(), 'abc\ndef\nxyzzy\nfoo\x1abar\n')
    self.assertTrue(f._rolled)
    self.assertEqual(f.mode, 'w+')
    self.assertIsNotNone(f.name)
    self.assertEqual(f.newlines, os.linesep)
    self.assertEqual(f.encoding, 'utf-8')
    self.assertEqual(f.errors, 'strict')
