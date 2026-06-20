# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copy2_xattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp_dir = self.mkdtemp()
    src = os.path.join(tmp_dir, 'foo')
    dst = os.path.join(tmp_dir, 'bar')
    write_file(src, 'foo')
    os.setxattr(src, 'user.foo', b'42')
    shutil.copy2(src, dst)
    self.assertEqual(os.getxattr(src, 'user.foo'), os.getxattr(dst, 'user.foo'))
    os.remove(dst)
