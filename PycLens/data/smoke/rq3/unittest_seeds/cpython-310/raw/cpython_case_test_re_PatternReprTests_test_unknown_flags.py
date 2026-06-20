# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: PatternReprTests_test_unknown_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_flags('random pattern', 1191936, "re.compile('random pattern', 0x123000)")
    self.check_flags('random pattern', 1191936 | re.I, "re.compile('random pattern', re.IGNORECASE|0x123000)")
