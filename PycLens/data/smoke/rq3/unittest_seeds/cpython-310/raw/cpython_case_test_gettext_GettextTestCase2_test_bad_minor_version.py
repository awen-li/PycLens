# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: GettextTestCase2_test_bad_minor_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(MOFILE_BAD_MINOR_VERSION, 'rb') as fp:
        gettext.GNUTranslations(fp)
