# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_dont_parse_argv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pre_config = {'parse_argv': 0}
    config = {'parse_argv': 0, 'argv': ['./argv0', '-E', '-c', 'pass', 'arg1', '-v', 'arg3'], 'orig_argv': ['./argv0', '-E', '-c', 'pass', 'arg1', '-v', 'arg3'], 'program_name': './argv0'}
    self.check_all_configs('test_init_dont_parse_argv', config, pre_config, api=API_PYTHON)
