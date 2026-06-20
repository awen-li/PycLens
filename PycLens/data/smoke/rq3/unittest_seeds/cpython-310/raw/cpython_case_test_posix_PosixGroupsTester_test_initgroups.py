# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixGroupsTester_test_initgroups

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g = max(self.saved_groups or [0]) + 1
    name = pwd.getpwuid(posix.getuid()).pw_name
    posix.initgroups(name, g)
    self.assertIn(g, posix.getgroups())
