# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_swap_std_fds_with_one_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for from_fds in itertools.combinations(range(3), 2):
        for to_fds in itertools.permutations(range(3), 2):
            self._check_swap_std_fds_with_one_closed(from_fds, to_fds)
