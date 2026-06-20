# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_cleanup_with_symlink_to_a_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = self.do_create()
    d2 = self.do_create(recurse=0)
    os.symlink(d2.name, os.path.join(d1.name, 'foo'))
    d1.cleanup()
    self.assertFalse(os.path.exists(d1.name), 'TemporaryDirectory %s exists after cleanup' % d1.name)
    self.assertTrue(os.path.exists(d2.name), 'Directory pointed to by a symlink was deleted')
    self.assertEqual(os.listdir(d2.name), ['test0.txt'], 'Contents of the directory pointed to by a symlink were deleted')
    d2.cleanup()
