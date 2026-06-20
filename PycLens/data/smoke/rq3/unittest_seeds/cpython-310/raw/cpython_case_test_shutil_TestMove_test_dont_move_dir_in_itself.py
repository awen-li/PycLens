# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_dont_move_dir_in_itself

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dst = os.path.join(self.src_dir, 'bar')
    self.assertRaises(shutil.Error, shutil.move, self.src_dir, dst)
