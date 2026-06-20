# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copystat_handles_harmless_chflags_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmpdir = self.mkdtemp()
    file1 = os.path.join(tmpdir, 'file1')
    file2 = os.path.join(tmpdir, 'file2')
    write_file(file1, 'xxx')
    write_file(file2, 'xxx')

    def make_chflags_raiser(err):
        ex = OSError()

        def _chflags_raiser(path, flags, *, follow_symlinks=True):
            ex.errno = err
            raise ex
        return _chflags_raiser
    old_chflags = os.chflags
    try:
        for err in (errno.EOPNOTSUPP, errno.ENOTSUP):
            os.chflags = make_chflags_raiser(err)
            shutil.copystat(file1, file2)
        os.chflags = make_chflags_raiser(errno.EOPNOTSUPP + errno.ENOTSUP)
        self.assertRaises(OSError, shutil.copystat, file1, file2)
    finally:
        os.chflags = old_chflags
