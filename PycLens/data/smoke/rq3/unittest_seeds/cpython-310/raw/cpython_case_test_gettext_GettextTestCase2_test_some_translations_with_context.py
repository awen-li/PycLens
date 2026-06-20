# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: GettextTestCase2_test_some_translations_with_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(gettext.pgettext('my context', 'nudge nudge'), 'wink wink (in "my context")')
    eq(gettext.pgettext('my other context', 'nudge nudge'), 'wink wink (in "my other context")')
