# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: PluralFormsTestCase_test_security

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raises = self.assertRaises
    raises(ValueError, gettext.c2py, "os.chmod('/etc/passwd',0777)")
    raises(ValueError, gettext.c2py, '"(eval(foo) && ""')
    raises(ValueError, gettext.c2py, 'f"{os.system(\'sh\')}"')
    raises(ValueError, gettext.c2py, 'n+' * 10000 + 'n')
    self.assertEqual(gettext.c2py('n+' * 100 + 'n')(1), 101)
    raises(ValueError, gettext.c2py, '(' * 100 + 'n' + ')' * 100)
    raises(ValueError, gettext.c2py, '(' * 10000 + 'n' + ')' * 10000)
    self.assertEqual(gettext.c2py('(' * 20 + 'n' + ')' * 20)(1), 1)
