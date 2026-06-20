# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: GettextTestCase2_test_bad_major_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(MOFILE_BAD_MAJOR_VERSION, 'rb') as fp:
        with self.assertRaises(OSError) as cm:
            gettext.GNUTranslations(fp)
        exception = cm.exception
        self.assertEqual(exception.errno, 0)
        self.assertEqual(exception.strerror, 'Bad version number 5')
        self.assertEqual(exception.filename, MOFILE_BAD_MAJOR_VERSION)
