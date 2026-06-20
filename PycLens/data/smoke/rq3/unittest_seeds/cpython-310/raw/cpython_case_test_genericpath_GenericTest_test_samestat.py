# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: GenericTest_test_samestat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_fn1 = os_helper.TESTFN
    test_fn2 = os_helper.TESTFN + '2'
    self.addCleanup(os_helper.unlink, test_fn1)
    self.addCleanup(os_helper.unlink, test_fn2)
    create_file(test_fn1)
    stat1 = os.stat(test_fn1)
    self.assertTrue(self.pathmodule.samestat(stat1, os.stat(test_fn1)))
    create_file(test_fn2)
    stat2 = os.stat(test_fn2)
    self.assertFalse(self.pathmodule.samestat(stat1, stat2))
    self.assertRaises(TypeError, self.pathmodule.samestat)
