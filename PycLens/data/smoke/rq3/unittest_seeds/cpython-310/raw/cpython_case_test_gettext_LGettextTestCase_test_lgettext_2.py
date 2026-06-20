# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: LGettextTestCase_test_lgettext_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.mofile, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
    lgettext = t.lgettext
    with self.assertDeprecated('lgettext'):
        self.assertEqual(lgettext('mullusk'), b'bacon')
    with self.assertDeprecated('lgettext'):
        self.assertEqual(lgettext('spam'), b'spam')
