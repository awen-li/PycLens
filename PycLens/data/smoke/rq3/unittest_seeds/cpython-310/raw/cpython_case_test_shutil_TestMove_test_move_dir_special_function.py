# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_move_dir_special_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    moved = []

    def _copy(src, dst):
        moved.append((src, dst))
    os_helper.create_empty_file(os.path.join(self.src_dir, 'child'))
    os_helper.create_empty_file(os.path.join(self.src_dir, 'child1'))
    shutil.move(self.src_dir, self.dst_dir, copy_function=_copy)
    self.assertEqual(len(moved), 3)
