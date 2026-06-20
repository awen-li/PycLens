# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_parse_argv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = {'parse_argv': 2, 'argv': ['-c', 'arg1', '-v', 'arg3'], 'orig_argv': ['./argv0', '-E', '-c', 'pass', 'arg1', '-v', 'arg3'], 'program_name': './argv0', 'run_command': 'pass\n', 'use_environment': 0}
    self.check_all_configs('test_init_parse_argv', config, api=API_PYTHON)
