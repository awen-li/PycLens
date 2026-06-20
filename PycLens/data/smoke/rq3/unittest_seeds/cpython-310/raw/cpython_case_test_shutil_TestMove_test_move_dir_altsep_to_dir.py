# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_move_dir_altsep_to_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_move_dir(self.src_dir + os.path.altsep, self.dst_dir, os.path.join(self.dst_dir, os.path.basename(self.src_dir)))
