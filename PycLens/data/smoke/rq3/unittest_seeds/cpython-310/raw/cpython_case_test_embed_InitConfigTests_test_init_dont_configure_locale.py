# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_dont_configure_locale

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    preconfig = {'configure_locale': 0, 'coerce_c_locale': 0}
    self.check_all_configs('test_init_dont_configure_locale', {}, preconfig, api=API_PYTHON)
