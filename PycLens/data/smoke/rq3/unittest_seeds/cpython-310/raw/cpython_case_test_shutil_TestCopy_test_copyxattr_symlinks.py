# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copyxattr_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp_dir = self.mkdtemp()
    src = os.path.join(tmp_dir, 'foo')
    src_link = os.path.join(tmp_dir, 'baz')
    write_file(src, 'foo')
    os.symlink(src, src_link)
    os.setxattr(src, 'trusted.foo', b'42')
    os.setxattr(src_link, 'trusted.foo', b'43', follow_symlinks=False)
    dst = os.path.join(tmp_dir, 'bar')
    dst_link = os.path.join(tmp_dir, 'qux')
    write_file(dst, 'bar')
    os.symlink(dst, dst_link)
    shutil._copyxattr(src_link, dst_link, follow_symlinks=False)
    self.assertEqual(os.getxattr(dst_link, 'trusted.foo', follow_symlinks=False), b'43')
    self.assertRaises(OSError, os.getxattr, dst, 'trusted.foo')
    shutil._copyxattr(src_link, dst, follow_symlinks=False)
    self.assertEqual(os.getxattr(dst, 'trusted.foo'), b'43')
