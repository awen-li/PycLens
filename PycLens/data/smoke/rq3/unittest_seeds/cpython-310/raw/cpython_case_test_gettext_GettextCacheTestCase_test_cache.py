# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: GettextCacheTestCase_test_cache

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.localedir = os.curdir
    self.mofile = MOFILE
    self.assertEqual(len(gettext._translations), 0)
    t = gettext.translation('gettext', self.localedir)
    self.assertEqual(len(gettext._translations), 1)
    t = gettext.translation('gettext', self.localedir, class_=DummyGNUTranslations)
    self.assertEqual(len(gettext._translations), 2)
    self.assertEqual(t.__class__, DummyGNUTranslations)
    t = gettext.translation('gettext', self.localedir, class_=DummyGNUTranslations)
    self.assertEqual(len(gettext._translations), 2)
    self.assertEqual(t.__class__, DummyGNUTranslations)
    with self.assertWarnsRegex(DeprecationWarning, 'parameter codeset'):
        t = gettext.translation('gettext', self.localedir, class_=DummyGNUTranslations, codeset='utf-16')
    self.assertEqual(len(gettext._translations), 2)
    self.assertEqual(t.__class__, DummyGNUTranslations)
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(t.output_charset(), 'utf-16')
