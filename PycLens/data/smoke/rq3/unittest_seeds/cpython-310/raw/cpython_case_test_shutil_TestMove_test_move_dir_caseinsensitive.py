# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_move_dir_caseinsensitive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.src_dir = self.mkdtemp()
    dst_dir = os.path.join(os.path.dirname(self.src_dir), os.path.basename(self.src_dir).upper())
    self.assertNotEqual(self.src_dir, dst_dir)
    try:
        shutil.move(self.src_dir, dst_dir)
        self.assertTrue(os.path.isdir(dst_dir))
    finally:
        os.rmdir(dst_dir)
