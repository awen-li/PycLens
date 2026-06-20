# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: CommonTest_test_expandvars_nonascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expandvars = self.pathmodule.expandvars

    def check(value, expected):
        self.assertEqual(expandvars(value), expected)
    with os_helper.EnvironmentVarGuard() as env:
        env.clear()
        nonascii = os_helper.FS_NONASCII
        env['spam'] = nonascii
        env[nonascii] = 'ham' + nonascii
        check(nonascii, nonascii)
        check('$spam bar', '%s bar' % nonascii)
        check('${spam}bar', '%sbar' % nonascii)
        check('${%s}bar' % nonascii, 'ham%sbar' % nonascii)
        check('$bar%s bar' % nonascii, '$bar%s bar' % nonascii)
        check('$spam}bar', '%s}bar' % nonascii)
        check(os.fsencode(nonascii), os.fsencode(nonascii))
        check(b'$spam bar', os.fsencode('%s bar' % nonascii))
        check(b'${spam}bar', os.fsencode('%sbar' % nonascii))
        check(os.fsencode('${%s}bar' % nonascii), os.fsencode('ham%sbar' % nonascii))
        check(os.fsencode('$bar%s bar' % nonascii), os.fsencode('$bar%s bar' % nonascii))
        check(b'$spam}bar', os.fsencode('%s}bar' % nonascii))
