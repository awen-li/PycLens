# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_empty_pattern

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(glob.glob(''), [])
    self.assertEqual(glob.glob(b''), [])
    self.assertEqual(glob.glob('', root_dir=self.tempdir), [])
    self.assertEqual(glob.glob(b'', root_dir=os.fsencode(self.tempdir)), [])
    self.assertEqual(glob.glob('', dir_fd=self.dir_fd), [])
    self.assertEqual(glob.glob(b'', dir_fd=self.dir_fd), [])
