# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: GenericTest_test_sameopenfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, filename)
    create_file(filename)
    with open(filename, 'rb', 0) as fp1:
        fd1 = fp1.fileno()
        with open(filename, 'rb', 0) as fp2:
            fd2 = fp2.fileno()
            self.assertTrue(self.pathmodule.sameopenfile(fd1, fd2))
