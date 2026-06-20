# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_sep_in_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    normsep = os.path.normcase('\\') == os.path.normcase('/')
    check = self.check_match
    check('a/b', 'a[.-0]b', not normsep)
    check('a\\b', 'a[.-0]b', False)
    check('a\\b', 'a[Z-^]b', not normsep)
    check('a/b', 'a[Z-^]b', False)
    check('a/b', 'a[/-0]b', not normsep)
    check('a\\b', 'a[/-0]b', False)
    check('a[/-0]b', 'a[/-0]b', False)
    check('a[\\-0]b', 'a[/-0]b', False)
    check('a/b', 'a[.-/]b')
    check('a\\b', 'a[.-/]b', normsep)
    check('a[.-/]b', 'a[.-/]b', False)
    check('a[.-\\]b', 'a[.-/]b', False)
    check('a\\b', 'a[\\-^]b')
    check('a/b', 'a[\\-^]b', normsep)
    check('a[\\-^]b', 'a[\\-^]b', False)
    check('a[/-^]b', 'a[\\-^]b', False)
    check('a\\b', 'a[Z-\\]b', not normsep)
    check('a/b', 'a[Z-\\]b', False)
    check('a[Z-\\]b', 'a[Z-\\]b', False)
    check('a[Z-/]b', 'a[Z-\\]b', False)
