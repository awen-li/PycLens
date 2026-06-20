# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copyfile_return_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    dst_dir = self.mkdtemp()
    dst_file = os.path.join(dst_dir, 'bar')
    src_file = os.path.join(src_dir, 'foo')
    write_file(src_file, 'foo')
    rv = shutil.copyfile(src_file, dst_file)
    self.assertTrue(os.path.exists(rv))
    self.assertEqual(read_file(src_file), read_file(dst_file))
