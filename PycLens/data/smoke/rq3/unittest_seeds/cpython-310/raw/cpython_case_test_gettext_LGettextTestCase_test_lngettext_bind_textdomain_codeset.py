# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: LGettextTestCase_test_lngettext_bind_textdomain_codeset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lngettext = gettext.lngettext
    ldngettext = gettext.ldngettext
    with self.assertDeprecated('bind_textdomain_codeset'):
        saved_codeset = gettext.bind_textdomain_codeset('gettext')
    try:
        with self.assertDeprecated('bind_textdomain_codeset'):
            gettext.bind_textdomain_codeset('gettext', 'utf-16')
        with self.assertDeprecated('lngettext'):
            x = lngettext('There is %s file', 'There are %s files', 1)
        self.assertEqual(x, 'Hay %s fichero'.encode('utf-16'))
        with self.assertDeprecated('lngettext'):
            x = lngettext('There is %s file', 'There are %s files', 2)
        self.assertEqual(x, 'Hay %s ficheros'.encode('utf-16'))
        with self.assertDeprecated('lngettext'):
            x = lngettext('There is %s directory', 'There are %s directories', 1)
        self.assertEqual(x, 'There is %s directory'.encode('utf-16'))
        with self.assertDeprecated('lngettext'):
            x = lngettext('There is %s directory', 'There are %s directories', 2)
        self.assertEqual(x, 'There are %s directories'.encode('utf-16'))
        with self.assertDeprecated('ldngettext'):
            x = ldngettext('gettext', 'There is %s file', 'There are %s files', 1)
        self.assertEqual(x, 'Hay %s fichero'.encode('utf-16'))
        with self.assertDeprecated('ldngettext'):
            x = ldngettext('gettext', 'There is %s file', 'There are %s files', 2)
        self.assertEqual(x, 'Hay %s ficheros'.encode('utf-16'))
        with self.assertDeprecated('ldngettext'):
            x = ldngettext('gettext', 'There is %s directory', 'There are %s directories', 1)
        self.assertEqual(x, 'There is %s directory'.encode('utf-16'))
        with self.assertDeprecated('ldngettext'):
            x = ldngettext('gettext', 'There is %s directory', 'There are %s directories', 2)
        self.assertEqual(x, 'There are %s directories'.encode('utf-16'))
    finally:
        del gettext._localecodesets['gettext']
        with self.assertDeprecated('bind_textdomain_codeset'):
            gettext.bind_textdomain_codeset('gettext', saved_codeset)
