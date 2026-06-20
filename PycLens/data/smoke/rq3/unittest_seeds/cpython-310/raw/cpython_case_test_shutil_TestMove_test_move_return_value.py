# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_move_return_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rv = shutil.move(self.src_file, self.dst_dir)
    self.assertEqual(rv, os.path.join(self.dst_dir, os.path.basename(self.src_file)))
