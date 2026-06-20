# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_slow_fnmatch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self.check_match
    check('a' * 50, '*a*a*a*a*a*a*a*a*a*a')
    check('a' * 50 + 'b', '*a*a*a*a*a*a*a*a*a*a', False)
