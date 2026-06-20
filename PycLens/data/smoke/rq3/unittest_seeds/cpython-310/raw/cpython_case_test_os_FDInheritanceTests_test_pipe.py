# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FDInheritanceTests_test_pipe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rfd, wfd) = os.pipe()
    self.addCleanup(os.close, rfd)
    self.addCleanup(os.close, wfd)
    self.assertEqual(os.get_inheritable(rfd), False)
    self.assertEqual(os.get_inheritable(wfd), False)
