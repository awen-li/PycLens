# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: LGettextTestCase_test_lgettext

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lgettext = gettext.lgettext
    ldgettext = gettext.ldgettext
    with self.assertDeprecated('lgettext'):
        self.assertEqual(lgettext('mullusk'), b'bacon')
    with self.assertDeprecated('lgettext'):
        self.assertEqual(lgettext('spam'), b'spam')
    with self.assertDeprecated('ldgettext'):
        self.assertEqual(ldgettext('gettext', 'mullusk'), b'bacon')
    with self.assertDeprecated('ldgettext'):
        self.assertEqual(ldgettext('gettext', 'spam'), b'spam')
