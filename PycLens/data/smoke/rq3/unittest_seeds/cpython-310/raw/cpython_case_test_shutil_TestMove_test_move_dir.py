# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_move_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dst_dir = tempfile.mktemp(dir=self.mkdtemp())
    try:
        self._check_move_dir(self.src_dir, dst_dir, dst_dir)
    finally:
        os_helper.rmtree(dst_dir)
