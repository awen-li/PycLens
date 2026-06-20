# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_sep_in_char_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    normsep = os.path.normcase('\\') == os.path.normcase('/')
    check = self.check_match
    check('/', '[/]')
    check('\\', '[\\]')
    check('/', '[\\]', normsep)
    check('\\', '[/]', normsep)
    check('[/]', '[/]', False)
    check('[\\\\]', '[/]', False)
    check('\\', '[\\t]')
    check('/', '[\\t]', normsep)
    check('t', '[\\t]')
    check('\t', '[\\t]', False)
