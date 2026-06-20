# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copyfile_named_pipe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.mkfifo(TESTFN)
    except PermissionError as e:
        self.skipTest('os.mkfifo(): %s' % e)
    try:
        self.assertRaises(shutil.SpecialFileError, shutil.copyfile, TESTFN, TESTFN2)
        self.assertRaises(shutil.SpecialFileError, shutil.copyfile, __file__, TESTFN)
    finally:
        os.remove(TESTFN)
