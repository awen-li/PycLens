# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_realpath_strict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ABSTFN = ntpath.abspath(os_helper.TESTFN)
    os.symlink(ABSTFN + '1', ABSTFN)
    self.addCleanup(os_helper.unlink, ABSTFN)
    self.assertRaises(FileNotFoundError, ntpath.realpath, ABSTFN, strict=True)
    self.assertRaises(FileNotFoundError, ntpath.realpath, ABSTFN + '2', strict=True)
