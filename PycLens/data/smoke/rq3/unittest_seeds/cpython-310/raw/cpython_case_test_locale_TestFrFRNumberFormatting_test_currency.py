# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestFrFRNumberFormatting_test_currency

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    euro = '€'
    self._test_currency(50000, '50000,00 ' + euro)
    self._test_currency(50000, '50 000,00 ' + euro, grouping=True)
    self._test_currency(50000, '50 000,00 EUR', grouping=True, international=True)
