# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fcntl.py
# case: TestFcntl_test_fcntl_f_getpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.f = open(TESTFN, 'wb')
    expected = os.path.abspath(TESTFN).encode('utf-8')
    res = fcntl.fcntl(self.f.fileno(), fcntl.F_GETPATH, bytes(len(expected)))
    self.assertEqual(expected, res)
