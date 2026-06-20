# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: UnicodeTranslationsPluralTest_test_unicode_context_msgid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unless = self.assertTrue
    unless(isinstance(self.npgettext('', '', '', 1), str))
    unless(isinstance(self.npgettext('', '', '', 2), str))
