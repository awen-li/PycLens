# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_case

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ignorecase = os.path.normcase('ABC') == os.path.normcase('abc')
    check = self.check_match
    check('abc', 'abc')
    check('AbC', 'abc', ignorecase)
    check('abc', 'AbC', ignorecase)
    check('AbC', 'AbC')
