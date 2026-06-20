# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_env_dev_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    preconfig = dict(allocator=PYMEM_ALLOCATOR_DEBUG)
    config = dict(dev_mode=1, faulthandler=1, warnoptions=['default'])
    self.check_all_configs('test_init_env_dev_mode', config, preconfig, api=API_COMPAT)
