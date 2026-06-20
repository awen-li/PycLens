# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copyxattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp_dir = self.mkdtemp()
    src = os.path.join(tmp_dir, 'foo')
    write_file(src, 'foo')
    dst = os.path.join(tmp_dir, 'bar')
    write_file(dst, 'bar')
    shutil._copyxattr(src, dst)
    os.setxattr(src, 'user.foo', b'42')
    os.setxattr(src, 'user.bar', b'43')
    shutil._copyxattr(src, dst)
    self.assertEqual(sorted(os.listxattr(src)), sorted(os.listxattr(dst)))
    self.assertEqual(os.getxattr(src, 'user.foo'), os.getxattr(dst, 'user.foo'))
    os.remove(dst)
    write_file(dst, 'bar')
    os_error = OSError(errno.EPERM, 'EPERM')

    def _raise_on_user_foo(fname, attr, val, **kwargs):
        if attr == 'user.foo':
            raise os_error
        else:
            orig_setxattr(fname, attr, val, **kwargs)
    try:
        orig_setxattr = os.setxattr
        os.setxattr = _raise_on_user_foo
        shutil._copyxattr(src, dst)
        self.assertIn('user.bar', os.listxattr(dst))
    finally:
        os.setxattr = orig_setxattr

    def _raise_on_src(fname, *, follow_symlinks=True):
        if fname == src:
            raise OSError(errno.ENOTSUP, 'Operation not supported')
        return orig_listxattr(fname, follow_symlinks=follow_symlinks)
    try:
        orig_listxattr = os.listxattr
        os.listxattr = _raise_on_src
        shutil._copyxattr(src, dst)
    finally:
        os.listxattr = orig_listxattr
    src = os.path.join(tmp_dir, 'the_original')
    srcro = os.path.join(tmp_dir, 'the_original_ro')
    write_file(src, src)
    write_file(srcro, srcro)
    os.setxattr(src, 'user.the_value', b'fiddly')
    os.setxattr(srcro, 'user.the_value', b'fiddly')
    os.chmod(srcro, 292)
    dst = os.path.join(tmp_dir, 'the_copy')
    dstro = os.path.join(tmp_dir, 'the_copy_ro')
    write_file(dst, dst)
    write_file(dstro, dstro)
    shutil.copystat(src, dst)
    shutil.copystat(srcro, dstro)
    self.assertEqual(os.getxattr(dst, 'user.the_value'), b'fiddly')
    self.assertEqual(os.getxattr(dstro, 'user.the_value'), b'fiddly')
