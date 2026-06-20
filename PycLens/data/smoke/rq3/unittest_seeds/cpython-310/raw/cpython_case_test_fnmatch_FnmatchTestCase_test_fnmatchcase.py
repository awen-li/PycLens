# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_fnmatchcase

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self.check_match
    check('abc', 'abc', True, fnmatchcase)
    check('AbC', 'abc', False, fnmatchcase)
    check('abc', 'AbC', False, fnmatchcase)
    check('AbC', 'AbC', True, fnmatchcase)
    check('usr/bin', 'usr/bin', True, fnmatchcase)
    check('usr\\bin', 'usr/bin', False, fnmatchcase)
    check('usr/bin', 'usr\\bin', False, fnmatchcase)
    check('usr\\bin', 'usr\\bin', True, fnmatchcase)
