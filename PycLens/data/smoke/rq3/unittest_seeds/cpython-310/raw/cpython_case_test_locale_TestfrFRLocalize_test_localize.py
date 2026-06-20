# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestfrFRLocalize_test_localize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_localize('50000.00', '50000,00')
    self._test_localize('50000.00', '50 000,00', grouping=True)
