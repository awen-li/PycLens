# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_relative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.symlink(posixpath.relpath(ABSTFN + '1'), ABSTFN)
        self.assertEqual(realpath(ABSTFN), ABSTFN + '1')
    finally:
        os_helper.unlink(ABSTFN)
