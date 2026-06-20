# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_access

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = os.open(os_helper.TESTFN, os.O_CREAT | os.O_RDWR)
    os.close(f)
    self.assertTrue(os.access(os_helper.TESTFN, os.W_OK))
