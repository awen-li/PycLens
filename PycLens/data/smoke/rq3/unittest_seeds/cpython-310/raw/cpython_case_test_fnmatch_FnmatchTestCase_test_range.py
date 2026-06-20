# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: FnmatchTestCase_test_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ignorecase = os.path.normcase('ABC') == os.path.normcase('abc')
    normsep = os.path.normcase('\\') == os.path.normcase('/')
    check = self.check_match
    tescases = string.ascii_lowercase + string.digits + string.punctuation
    for c in tescases:
        check(c, '[b-d]', c in 'bcd')
        check(c, '[!b-d]', c not in 'bcd')
        check(c, '[b-dx-z]', c in 'bcdxyz')
        check(c, '[!b-dx-z]', c not in 'bcdxyz')
    for c in tescases:
        check(c, '[B-D]', c in 'bcd' and ignorecase)
        check(c, '[!B-D]', c not in 'bcd' or not ignorecase)
    for c in string.ascii_uppercase:
        check(c, '[b-d]', c in 'BCD' and ignorecase)
        check(c, '[!b-d]', c not in 'BCD' or not ignorecase)
    for c in tescases:
        check(c, '[b-b]', c == 'b')
    for c in tescases:
        check(c, '[!-#]', c not in '-#')
        check(c, '[!--.]', c not in '-.')
        check(c, '[^-`]', c in '^_`')
        if not (normsep and c == '/'):
            check(c, '[[-^]', c in '[\\]^')
            check(c, '[\\-^]', c in '\\]^')
        check(c, '[b-]', c in '-b')
        check(c, '[!b-]', c not in '-b')
        check(c, '[-b]', c in '-b')
        check(c, '[!-b]', c not in '-b')
        check(c, '[-]', c in '-')
        check(c, '[!-]', c not in '-')
    for c in tescases:
        check(c, '[d-b]', False)
        check(c, '[!d-b]', True)
        check(c, '[d-bx-z]', c in 'xyz')
        check(c, '[!d-bx-z]', c not in 'xyz')
        check(c, '[d-b^-`]', c in '^_`')
        if not (normsep and c == '/'):
            check(c, '[d-b[-^]', c in '[\\]^')
