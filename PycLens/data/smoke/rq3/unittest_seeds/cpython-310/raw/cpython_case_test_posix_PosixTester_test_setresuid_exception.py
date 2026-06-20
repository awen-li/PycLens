# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_setresuid_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    current_user_ids = posix.getresuid()
    if 0 not in current_user_ids:
        new_user_ids = (current_user_ids[0] + 1, -1, -1)
        self.assertRaises(OSError, posix.setresuid, *new_user_ids)
