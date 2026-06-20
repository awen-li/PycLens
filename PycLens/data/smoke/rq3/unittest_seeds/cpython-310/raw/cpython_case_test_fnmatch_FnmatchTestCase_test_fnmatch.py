# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_fnmatch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self.check_match
    check('abc', 'abc')
    check('abc', '?*?')
    check('abc', '???*')
    check('abc', '*???')
    check('abc', '???')
    check('abc', '*')
    check('abc', 'ab[cd]')
    check('abc', 'ab[!de]')
    check('abc', 'ab[de]', False)
    check('a', '??', False)
    check('a', 'b', False)
    check('\\', '[\\]')
    check('a', '[!\\]')
    check('\\', '[!\\]', False)
    check('foo\nbar', 'foo*')
    check('foo\nbar\n', 'foo*')
    check('\nfoo', 'foo*', False)
    check('\n', '*')
