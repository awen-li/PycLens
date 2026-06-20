# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_realpath_relative

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ABSTFN = ntpath.abspath(os_helper.TESTFN)
    open(ABSTFN, 'wb').close()
    self.addCleanup(os_helper.unlink, ABSTFN)
    self.addCleanup(os_helper.unlink, ABSTFN + '1')
    os.symlink(ABSTFN, ntpath.relpath(ABSTFN + '1'))
    self.assertPathEqual(ntpath.realpath(ABSTFN + '1'), ABSTFN)
