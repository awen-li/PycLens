# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FDInheritanceTests_test_dup_standard_stream

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.dup(1)
    self.addCleanup(os.close, fd)
    self.assertGreater(fd, 0)
