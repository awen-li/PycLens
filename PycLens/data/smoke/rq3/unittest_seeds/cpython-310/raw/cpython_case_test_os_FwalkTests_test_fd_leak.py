# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FwalkTests_test_fd_leak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    minfd = os.dup(1)
    os.close(minfd)
    for i in range(256):
        for x in self.fwalk(os_helper.TESTFN):
            pass
    newfd = os.dup(1)
    self.addCleanup(os.close, newfd)
    self.assertEqual(newfd, minfd)
