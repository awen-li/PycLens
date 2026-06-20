# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copyfile_nonexistent_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    src_file = os.path.join(src_dir, 'foo')
    dst = os.path.join(src_dir, 'does_not_exist/')
    write_file(src_file, 'foo')
    self.assertRaises(FileNotFoundError, shutil.copyfile, src_file, dst)
