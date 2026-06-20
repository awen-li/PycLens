# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_expandvars_nonascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(value, expected):
        tester('ntpath.expandvars(%r)' % value, expected)
    with os_helper.EnvironmentVarGuard() as env:
        env.clear()
        nonascii = os_helper.FS_NONASCII
        env['spam'] = nonascii
        env[nonascii] = 'ham' + nonascii
        check('$spam bar', '%s bar' % nonascii)
        check('$%s bar' % nonascii, '$%s bar' % nonascii)
        check('${spam}bar', '%sbar' % nonascii)
        check('${%s}bar' % nonascii, 'ham%sbar' % nonascii)
        check('$spam}bar', '%s}bar' % nonascii)
        check('$%s}bar' % nonascii, '$%s}bar' % nonascii)
        check('%spam% bar', '%s bar' % nonascii)
        check('%{}% bar'.format(nonascii), 'ham%s bar' % nonascii)
        check('%spam%bar', '%sbar' % nonascii)
        check('%{}%bar'.format(nonascii), 'ham%sbar' % nonascii)
