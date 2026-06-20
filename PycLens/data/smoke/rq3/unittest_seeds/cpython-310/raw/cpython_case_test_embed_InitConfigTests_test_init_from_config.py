# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_from_config

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    preconfig = {'allocator': PYMEM_ALLOCATOR_MALLOC, 'utf8_mode': 1}
    config = {'install_signal_handlers': 0, 'use_hash_seed': 1, 'hash_seed': 123, 'tracemalloc': 2, 'import_time': 1, 'show_ref_count': 1, 'malloc_stats': 1, 'stdio_encoding': 'iso8859-1', 'stdio_errors': 'replace', 'pycache_prefix': 'conf_pycache_prefix', 'program_name': './conf_program_name', 'argv': ['-c', 'arg2'], 'orig_argv': ['python3', '-W', 'cmdline_warnoption', '-X', 'cmdline_xoption', '-c', 'pass', 'arg2'], 'parse_argv': 2, 'xoptions': ['config_xoption1=3', 'config_xoption2=', 'config_xoption3', 'cmdline_xoption'], 'warnoptions': ['cmdline_warnoption', 'default::BytesWarning', 'config_warnoption'], 'run_command': 'pass\n', 'site_import': 0, 'bytes_warning': 1, 'inspect': 1, 'interactive': 1, 'optimization_level': 2, 'write_bytecode': 0, 'verbose': 1, 'quiet': 1, 'configure_c_stdio': 1, 'buffered_stdio': 0, 'user_site_directory': 0, 'faulthandler': 1, 'platlibdir': 'my_platlibdir', 'module_search_paths': self.IGNORE_CONFIG, 'check_hash_pycs_mode': 'always', 'pathconfig_warnings': 0, '_isolated_interpreter': 1}
    self.check_all_configs('test_init_from_config', config, preconfig, api=API_COMPAT)
