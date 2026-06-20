# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_setresgid_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    current_group_ids = posix.getresgid()
    if 0 not in current_group_ids:
        new_group_ids = (current_group_ids[0] + 1, -1, -1)
        self.assertRaises(OSError, posix.setresgid, *new_group_ids)
