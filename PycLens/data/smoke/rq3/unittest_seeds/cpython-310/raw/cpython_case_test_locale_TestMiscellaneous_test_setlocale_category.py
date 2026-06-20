# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestMiscellaneous_test_setlocale_category

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    locale.setlocale(locale.LC_ALL)
    locale.setlocale(locale.LC_TIME)
    locale.setlocale(locale.LC_CTYPE)
    locale.setlocale(locale.LC_COLLATE)
    locale.setlocale(locale.LC_MONETARY)
    locale.setlocale(locale.LC_NUMERIC)
    self.assertRaises(locale.Error, locale.setlocale, 12345)
