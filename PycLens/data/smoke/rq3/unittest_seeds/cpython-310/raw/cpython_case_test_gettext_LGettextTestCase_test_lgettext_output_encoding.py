# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: LGettextTestCase_test_lgettext_output_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    lgettext = t.lgettext
    with self.assertDeprecated('set_output_charset'):
        t.set_output_charset('utf-16')
    with self.assertDeprecated('lgettext'):
        self.assertEqual(lgettext('mullusk'), 'bacon'.encode('utf-16'))
    with self.assertDeprecated('lgettext'):
        self.assertEqual(lgettext('spam'), 'spam'.encode('utf-16'))
