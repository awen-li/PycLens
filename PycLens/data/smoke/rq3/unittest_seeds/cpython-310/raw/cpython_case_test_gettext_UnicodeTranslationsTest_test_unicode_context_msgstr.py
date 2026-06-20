# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: UnicodeTranslationsTest_test_unicode_context_msgstr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.pgettext('mycontextÞ', 'abÞ')
    self.assertTrue(isinstance(t, str))
    self.assertEqual(t, '¤yz (context version)')
