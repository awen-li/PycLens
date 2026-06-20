# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_move_file_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dst = os.path.join(self.src_dir, 'bar')
    os.symlink(self.src_file, dst)
    shutil.move(dst, self.dst_file)
    self.assertTrue(os.path.islink(self.dst_file))
    self.assertTrue(os.path.samefile(self.src_file, self.dst_file))
