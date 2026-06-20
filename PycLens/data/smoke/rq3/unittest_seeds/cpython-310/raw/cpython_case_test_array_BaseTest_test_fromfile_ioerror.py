# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_fromfile_ioerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode)
    f = open(os_helper.TESTFN, 'wb')
    try:
        self.assertRaises(OSError, a.fromfile, f, len(self.example))
    finally:
        f.close()
        os_helper.unlink(os_helper.TESTFN)
