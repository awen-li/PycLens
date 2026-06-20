# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for flag in [re.I, re.M, re.X, re.S, re.A, re.U]:
        self.assertTrue(re.compile('^pattern$', flag))
    for flag in [re.I, re.M, re.X, re.S, re.A, re.L]:
        self.assertTrue(re.compile(b'^pattern$', flag))
