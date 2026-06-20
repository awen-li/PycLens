# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestSpooledTemporaryFile_test_truncate_with_size_parameter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = tempfile.SpooledTemporaryFile(max_size=10)
    f.write(b'abcdefg\n')
    f.seek(0)
    f.truncate()
    self.assertFalse(f._rolled)
    self.assertEqual(f._file.getvalue(), b'')
    f = tempfile.SpooledTemporaryFile(max_size=10)
    f.write(b'abcdefg\n')
    f.truncate(4)
    self.assertFalse(f._rolled)
    self.assertEqual(f._file.getvalue(), b'abcd')
    f = tempfile.SpooledTemporaryFile(max_size=10)
    f.write(b'abcdefg\n')
    f.truncate(20)
    self.assertTrue(f._rolled)
    self.assertEqual(os.fstat(f.fileno()).st_size, 20)
