# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestMove_test_move_dangling_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = os.path.join(self.src_dir, 'baz')
    dst = os.path.join(self.src_dir, 'bar')
    os.symlink(src, dst)
    dst_link = os.path.join(self.dst_dir, 'quux')
    shutil.move(dst, dst_link)
    self.assertTrue(os.path.islink(dst_link))
    self.assertEqual(os.path.realpath(src), os.path.realpath(dst_link))
