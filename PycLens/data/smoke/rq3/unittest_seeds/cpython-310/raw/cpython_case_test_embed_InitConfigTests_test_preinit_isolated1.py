# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_preinit_isolated1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = {'isolated': 1, 'use_environment': 0, 'user_site_directory': 0}
    self.check_all_configs('test_preinit_isolated1', config, api=API_COMPAT)
