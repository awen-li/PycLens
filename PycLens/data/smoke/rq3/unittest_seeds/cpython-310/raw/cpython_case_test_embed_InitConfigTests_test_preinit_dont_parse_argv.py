# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_preinit_dont_parse_argv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    preconfig = {'isolated': 0}
    argv = ['python3', '-E', '-I', '-X', 'dev', '-X', 'utf8', 'script.py']
    config = {'argv': argv, 'orig_argv': argv, 'isolated': 0}
    self.check_all_configs('test_preinit_dont_parse_argv', config, preconfig, api=API_ISOLATED)
