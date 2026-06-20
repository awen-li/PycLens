# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_move_file_to_dir_pathlike_src

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = pathlib.Path(self.src_file)
    self._check_move_file(src, self.dst_dir, self.dst_file)
