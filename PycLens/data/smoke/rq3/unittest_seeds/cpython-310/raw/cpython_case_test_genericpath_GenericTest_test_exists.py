# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: GenericTest_test_exists

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    bfilename = os.fsencode(filename)
    self.addCleanup(os_helper.unlink, filename)
    self.assertIs(self.pathmodule.exists(filename), False)
    self.assertIs(self.pathmodule.exists(bfilename), False)
    create_file(filename)
    self.assertIs(self.pathmodule.exists(filename), True)
    self.assertIs(self.pathmodule.exists(bfilename), True)
    self.assertIs(self.pathmodule.exists(filename + '\udfff'), False)
    self.assertIs(self.pathmodule.exists(bfilename + b'\xff'), False)
    self.assertIs(self.pathmodule.exists(filename + '\x00'), False)
    self.assertIs(self.pathmodule.exists(bfilename + b'\x00'), False)
    if self.pathmodule is not genericpath:
        self.assertIs(self.pathmodule.lexists(filename), True)
        self.assertIs(self.pathmodule.lexists(bfilename), True)
        self.assertIs(self.pathmodule.lexists(filename + '\udfff'), False)
        self.assertIs(self.pathmodule.lexists(bfilename + b'\xff'), False)
        self.assertIs(self.pathmodule.lexists(filename + '\x00'), False)
        self.assertIs(self.pathmodule.lexists(bfilename + b'\x00'), False)
