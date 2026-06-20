# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_getgrouplist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    user = pwd.getpwuid(os.getuid())[0]
    group = pwd.getpwuid(os.getuid())[3]
    self.assertIn(group, posix.getgrouplist(user, group))
