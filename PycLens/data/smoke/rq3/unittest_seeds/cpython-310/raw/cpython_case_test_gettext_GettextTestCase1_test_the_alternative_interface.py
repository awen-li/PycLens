# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: GettextTestCase1_test_the_alternative_interface

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    with open(self.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    t.install()
    eq(_('nudge nudge'), 'wink wink')
    t.install()
    eq(_('mullusk'), 'bacon')
    import builtins
    t.install(names=['gettext', 'lgettext'])
    eq(_, t.gettext)
    eq(builtins.gettext, t.gettext)
    eq(lgettext, t.lgettext)
    del builtins.gettext
    del builtins.lgettext
