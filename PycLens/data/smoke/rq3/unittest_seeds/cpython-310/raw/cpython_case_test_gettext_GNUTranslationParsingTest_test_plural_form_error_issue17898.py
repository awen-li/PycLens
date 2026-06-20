# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: GNUTranslationParsingTest_test_plural_form_error_issue17898

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(MOFILE, 'wb') as fp:
        fp.write(base64.decodebytes(GNU_MO_DATA_ISSUE_17898))
    with open(MOFILE, 'rb') as fp:
        t = gettext.GNUTranslations(fp)
