# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_match(b'test', b'te*')
    self.check_match(b'test\xff', b'te*\xff')
    self.check_match(b'foo\nbar', b'foo*')
