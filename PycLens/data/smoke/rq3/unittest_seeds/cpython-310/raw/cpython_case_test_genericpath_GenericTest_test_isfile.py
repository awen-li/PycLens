# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: GenericTest_test_isfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    bfilename = os.fsencode(filename)
    self.assertIs(self.pathmodule.isfile(filename), False)
    self.assertIs(self.pathmodule.isfile(bfilename), False)
    self.assertIs(self.pathmodule.isfile(filename + '\udfff'), False)
    self.assertIs(self.pathmodule.isfile(bfilename + b'\xff'), False)
    self.assertIs(self.pathmodule.isfile(filename + '\x00'), False)
    self.assertIs(self.pathmodule.isfile(bfilename + b'\x00'), False)
    try:
        create_file(filename)
        self.assertIs(self.pathmodule.isfile(filename), True)
        self.assertIs(self.pathmodule.isfile(bfilename), True)
    finally:
        os_helper.unlink(filename)
    try:
        os.mkdir(filename)
        self.assertIs(self.pathmodule.isfile(filename), False)
        self.assertIs(self.pathmodule.isfile(bfilename), False)
    finally:
        os_helper.rmdir(filename)
