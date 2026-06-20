# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_set_config

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = {'_init_main': 0, 'bytes_warning': 2, 'warnoptions': ['error::BytesWarning']}
    self.check_all_configs('test_init_set_config', config, api=API_ISOLATED)
