# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: UnicodeTranslationsPluralTest_test_unicode_msgid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unless = self.assertTrue
    unless(isinstance(self.ngettext('', '', 1), str))
    unless(isinstance(self.ngettext('', '', 2), str))
