# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: _ZeroCopyFileTest_test_unhandled_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with unittest.mock.patch(self.PATCHPOINT, side_effect=ZeroDivisionError):
        self.assertRaises(ZeroDivisionError, shutil.copyfile, TESTFN, TESTFN2)
