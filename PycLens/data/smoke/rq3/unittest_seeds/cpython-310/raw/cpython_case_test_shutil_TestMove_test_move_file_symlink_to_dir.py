# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_move_file_symlink_to_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = 'bar'
    dst = os.path.join(self.src_dir, filename)
    os.symlink(self.src_file, dst)
    shutil.move(dst, self.dst_dir)
    final_link = os.path.join(self.dst_dir, filename)
    self.assertTrue(os.path.islink(final_link))
    self.assertTrue(os.path.samefile(self.src_file, final_link))
