# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: PatternReprTests_test_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check(b'bytes pattern', "re.compile(b'bytes pattern')")
    self.check_flags(b'bytes pattern', re.A, "re.compile(b'bytes pattern', re.ASCII)")
