# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_c_locale_coercion.py
# case: LocaleCoercionTests_test_PYTHONCOERCECLOCALE_not_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for setting in ('', '1', 'true', 'false'):
        self._check_c_locale_coercion('utf-8', 'utf-8', coerce_c_locale=setting)
