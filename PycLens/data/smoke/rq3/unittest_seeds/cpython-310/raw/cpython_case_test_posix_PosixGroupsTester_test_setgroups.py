# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixGroupsTester_test_setgroups

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for groups in [[0], list(range(16))]:
        posix.setgroups(groups)
        self.assertListEqual(groups, posix.getgroups())
