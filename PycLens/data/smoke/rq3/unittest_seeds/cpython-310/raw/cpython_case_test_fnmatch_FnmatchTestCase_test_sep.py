# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_sep

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    normsep = os.path.normcase('\\') == os.path.normcase('/')
    check = self.check_match
    check('usr/bin', 'usr/bin')
    check('usr\\bin', 'usr/bin', normsep)
    check('usr/bin', 'usr\\bin', normsep)
    check('usr\\bin', 'usr\\bin')
