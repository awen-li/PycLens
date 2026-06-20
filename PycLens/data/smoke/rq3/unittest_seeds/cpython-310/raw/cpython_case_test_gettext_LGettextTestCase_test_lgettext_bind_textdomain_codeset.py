# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: LGettextTestCase_test_lgettext_bind_textdomain_codeset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lgettext = gettext.lgettext
    ldgettext = gettext.ldgettext
    with self.assertDeprecated('bind_textdomain_codeset'):
        saved_codeset = gettext.bind_textdomain_codeset('gettext')
    try:
        with self.assertDeprecated('bind_textdomain_codeset'):
            gettext.bind_textdomain_codeset('gettext', 'utf-16')
        with self.assertDeprecated('lgettext'):
            self.assertEqual(lgettext('mullusk'), 'bacon'.encode('utf-16'))
        with self.assertDeprecated('lgettext'):
            self.assertEqual(lgettext('spam'), 'spam'.encode('utf-16'))
        with self.assertDeprecated('ldgettext'):
            self.assertEqual(ldgettext('gettext', 'mullusk'), 'bacon'.encode('utf-16'))
        with self.assertDeprecated('ldgettext'):
            self.assertEqual(ldgettext('gettext', 'spam'), 'spam'.encode('utf-16'))
    finally:
        del gettext._localecodesets['gettext']
        with self.assertDeprecated('bind_textdomain_codeset'):
            gettext.bind_textdomain_codeset('gettext', saved_codeset)
