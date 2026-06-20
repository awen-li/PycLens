# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_gnu.py
# case: TestGdbm_test_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    all = set(gdbm.open_flags)
    modes = all - set('fsu')
    for mode in sorted(modes):
        self.g = gdbm.open(filename, mode)
        self.g.close()
    flags = all - set('crwn')
    for mode in modes:
        for flag in flags:
            self.g = gdbm.open(filename, mode + flag)
            self.g.close()
