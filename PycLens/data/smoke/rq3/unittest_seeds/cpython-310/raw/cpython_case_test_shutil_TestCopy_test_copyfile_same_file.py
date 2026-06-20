# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copyfile_same_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    src_file = os.path.join(src_dir, 'foo')
    write_file(src_file, 'foo')
    self.assertRaises(SameFileError, shutil.copyfile, src_file, src_file)
    self.assertRaises(Error, shutil.copyfile, src_file, src_file)
    self.assertEqual(read_file(src_file), 'foo')
