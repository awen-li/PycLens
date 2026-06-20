# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import _testinternalcapi, json; print(json.dumps(_testinternalcapi.get_configs()))'
    config = {'argv': ['-c', 'arg2'], 'orig_argv': ['python3', '-c', code, 'arg2'], 'program_name': './python3', 'run_command': code + '\n', 'parse_argv': 2, '_init_main': 0}
    self.check_all_configs('test_init_main', config, api=API_PYTHON, stderr='Run Python code before _Py_InitializeMain')
