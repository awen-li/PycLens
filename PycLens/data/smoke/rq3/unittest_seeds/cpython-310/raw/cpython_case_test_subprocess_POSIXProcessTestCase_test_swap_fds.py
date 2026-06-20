# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_swap_fds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_swap_fds(0, 1, 2)
    self.check_swap_fds(0, 2, 1)
    self.check_swap_fds(1, 0, 2)
    self.check_swap_fds(1, 2, 0)
    self.check_swap_fds(2, 0, 1)
    self.check_swap_fds(2, 1, 0)
