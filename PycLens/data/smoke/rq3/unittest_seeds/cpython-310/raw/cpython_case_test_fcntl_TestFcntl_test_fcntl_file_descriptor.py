# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fcntl.py
# case: TestFcntl_test_fcntl_file_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.f = open(TESTFN, 'wb')
    rv = fcntl.fcntl(self.f, fcntl.F_SETFL, os.O_NONBLOCK)
    if verbose:
        print('Status from fcntl with O_NONBLOCK: ', rv)
    rv = fcntl.fcntl(self.f, fcntl.F_SETLKW, lockdata)
    if verbose:
        print('String from fcntl with F_SETLKW: ', repr(rv))
    self.f.close()
