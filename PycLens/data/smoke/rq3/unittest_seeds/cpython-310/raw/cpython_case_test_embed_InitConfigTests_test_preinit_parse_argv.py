# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_preinit_parse_argv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    preconfig = {'allocator': PYMEM_ALLOCATOR_DEBUG}
    config = {'argv': ['script.py'], 'orig_argv': ['python3', '-X', 'dev', 'script.py'], 'run_filename': os.path.abspath('script.py'), 'dev_mode': 1, 'faulthandler': 1, 'warnoptions': ['default'], 'xoptions': ['dev']}
    self.check_all_configs('test_preinit_parse_argv', config, preconfig, api=API_PYTHON)
