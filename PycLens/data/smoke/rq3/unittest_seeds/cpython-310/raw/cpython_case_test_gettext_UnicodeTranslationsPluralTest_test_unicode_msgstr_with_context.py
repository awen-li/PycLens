# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: UnicodeTranslationsPluralTest_test_unicode_msgstr_with_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    unless = self.assertTrue
    t = self.npgettext('With context', 'There is %s file', 'There are %s files', 1)
    unless(isinstance(t, str))
    eq(t, 'Hay %s fichero (context)')
    t = self.npgettext('With context', 'There is %s file', 'There are %s files', 5)
    unless(isinstance(t, str))
    eq(t, 'Hay %s ficheros (context)')
