# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: GenericTest_test_samefile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    file1 = os_helper.TESTFN
    file2 = os_helper.TESTFN + '2'
    self.addCleanup(os_helper.unlink, file1)
    self.addCleanup(os_helper.unlink, file2)
    create_file(file1)
    self.assertTrue(self.pathmodule.samefile(file1, file1))
    create_file(file2)
    self.assertFalse(self.pathmodule.samefile(file1, file2))
    self.assertRaises(TypeError, self.pathmodule.samefile)
