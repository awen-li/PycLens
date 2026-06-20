# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_c_locale_coercion.py
# case: LocaleConfigurationTests_test_external_target_locale_configuration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.maxDiff = None
    expected_fs_encoding = 'utf-8'
    expected_stream_encoding = 'utf-8'
    base_var_dict = {'LANG': '', 'LC_CTYPE': '', 'LC_ALL': '', 'PYTHONCOERCECLOCALE': ''}
    for env_var in ('LANG', 'LC_CTYPE'):
        for locale_to_set in AVAILABLE_TARGETS:
            if env_var == 'LANG' and locale_to_set == 'UTF-8':
                continue
            with self.subTest(env_var=env_var, configured_locale=locale_to_set):
                var_dict = base_var_dict.copy()
                var_dict[env_var] = locale_to_set
                self._check_child_encoding_details(var_dict, expected_fs_encoding, expected_stream_encoding, expected_warnings=None, coercion_expected=False)
