# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: LGettextTestCase_test_lngettext_output_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    lngettext = t.lngettext
    with self.assertDeprecated('set_output_charset'):
        t.set_output_charset('utf-16')
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
