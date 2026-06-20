# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: LGettextTestCase_test_lngettext_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    lngettext = t.lngettext
    with self.assertDeprecated('lngettext'):
        x = lngettext('There is %s file', 'There are %s files', 1)
    self.assertEqual(x, b'Hay %s fichero')
    with self.assertDeprecated('lngettext'):
        x = lngettext('There is %s file', 'There are %s files', 2)
    self.assertEqual(x, b'Hay %s ficheros')
    with self.assertDeprecated('lngettext'):
        x = lngettext('There is %s directory', 'There are %s directories', 1)
    self.assertEqual(x, b'There is %s directory')
    with self.assertDeprecated('lngettext'):
        x = lngettext('There is %s directory', 'There are %s directories', 2)
    self.assertEqual(x, b'There are %s directories')
