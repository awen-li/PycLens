# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copyfile_copy_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    src_file = os.path.join(src_dir, 'foo')
    dir2 = self.mkdtemp()
    dst = os.path.join(src_dir, 'does_not_exist/')
    write_file(src_file, 'foo')
    if sys.platform == 'win32':
        err = PermissionError
    else:
        err = IsADirectoryError
    self.assertRaises(err, shutil.copyfile, src_dir, dst)
    self.assertRaises(err, shutil.copyfile, src_file, src_dir)
    self.assertRaises(err, shutil.copyfile, dir2, src_dir)
