# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_multi_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.open(os_helper.TESTFN, 'wb', buffering=0)
    f.close()
    f.close()
    f.close()
    self.assertRaises(ValueError, f.flush)
