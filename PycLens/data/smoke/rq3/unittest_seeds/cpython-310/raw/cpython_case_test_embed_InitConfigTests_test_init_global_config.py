# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_global_config

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    preconfig = {'utf8_mode': 1}
    config = {'program_name': './globalvar', 'site_import': 0, 'bytes_warning': 1, 'warnoptions': ['default::BytesWarning'], 'inspect': 1, 'interactive': 1, 'optimization_level': 2, 'write_bytecode': 0, 'verbose': 1, 'quiet': 1, 'buffered_stdio': 0, 'user_site_directory': 0, 'pathconfig_warnings': 0}
    self.check_all_configs('test_init_global_config', config, preconfig, api=API_COMPAT)
