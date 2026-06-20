# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_char_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ignorecase = os.path.normcase('ABC') == os.path.normcase('abc')
    check = self.check_match
    tescases = string.ascii_lowercase + string.digits + string.punctuation
    for c in tescases:
        check(c, '[az]', c in 'az')
        check(c, '[!az]', c not in 'az')
    for c in tescases:
        check(c, '[AZ]', c in 'az' and ignorecase)
        check(c, '[!AZ]', c not in 'az' or not ignorecase)
    for c in string.ascii_uppercase:
        check(c, '[az]', c in 'AZ' and ignorecase)
        check(c, '[!az]', c not in 'AZ' or not ignorecase)
    for c in tescases:
        check(c, '[aa]', c == 'a')
    for c in tescases:
        check(c, '[^az]', c in '^az')
        check(c, '[[az]', c in '[az')
        check(c, '[!]]', c != ']')
    check('[', '[')
    check('[]', '[]')
    check('[!', '[!')
    check('[!]', '[!]')
