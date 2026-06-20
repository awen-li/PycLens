# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_init_with_x_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(unlink, TESTFN)
    for mode in ('x', 'xb'):
        unlink(TESTFN)
        with LZMAFile(TESTFN, mode):
            pass
        with self.assertRaises(FileExistsError):
            with LZMAFile(TESTFN, mode):
                pass
