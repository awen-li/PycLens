# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: PatternReprTests_test_unicode_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_flags('random pattern', re.U, "re.compile('random pattern')")
    self.check_flags('random pattern', re.I | re.S | re.U, "re.compile('random pattern', re.IGNORECASE|re.DOTALL)")
