# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: GenericTest_test_getsize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, filename)
    create_file(filename, b'Hello')
    self.assertEqual(self.pathmodule.getsize(filename), 5)
    os.remove(filename)
    create_file(filename, b'Hello World!')
    self.assertEqual(self.pathmodule.getsize(filename), 12)
