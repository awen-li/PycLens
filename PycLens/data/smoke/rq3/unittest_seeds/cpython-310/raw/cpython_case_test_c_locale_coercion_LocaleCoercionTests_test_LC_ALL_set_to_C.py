# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_c_locale_coercion.py
# case: LocaleCoercionTests_test_LC_ALL_set_to_C

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_c_locale_coercion(EXPECTED_C_LOCALE_FS_ENCODING, EXPECTED_C_LOCALE_STREAM_ENCODING, coerce_c_locale=None, LC_ALL='C', coercion_expected=False)
    self._check_c_locale_coercion(EXPECTED_C_LOCALE_FS_ENCODING, EXPECTED_C_LOCALE_STREAM_ENCODING, coerce_c_locale='warn', LC_ALL='C', expected_warnings=[LEGACY_LOCALE_WARNING], coercion_expected=False)
