# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: PluralFormsTestCase_test_plural_forms2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    with open(self.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    x = t.ngettext('There is %s file', 'There are %s files', 1)
    eq(x, 'Hay %s fichero')
    x = t.ngettext('There is %s file', 'There are %s files', 2)
    eq(x, 'Hay %s ficheros')
