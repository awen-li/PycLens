# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_setresgid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    current_group_ids = posix.getresgid()
    self.assertIsNone(posix.setresgid(*current_group_ids))
    self.assertIsNone(posix.setresgid(-1, -1, -1))
