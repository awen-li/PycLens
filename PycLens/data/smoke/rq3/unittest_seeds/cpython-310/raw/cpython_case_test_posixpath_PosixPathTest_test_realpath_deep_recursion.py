# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_deep_recursion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    depth = 10
    try:
        os.mkdir(ABSTFN)
        for i in range(depth):
            os.symlink('/'.join(['%d' % i] * 10), ABSTFN + '/%d' % (i + 1))
        os.symlink('.', ABSTFN + '/0')
        self.assertEqual(realpath(ABSTFN + '/%d' % depth), ABSTFN)
        with os_helper.change_cwd(ABSTFN):
            self.assertEqual(realpath('%d' % depth), ABSTFN)
    finally:
        for i in range(depth + 1):
            os_helper.unlink(ABSTFN + '/%d' % i)
        safe_rmdir(ABSTFN)
