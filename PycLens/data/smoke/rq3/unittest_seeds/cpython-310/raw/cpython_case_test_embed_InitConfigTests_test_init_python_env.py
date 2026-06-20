# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_python_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    preconfig = {'allocator': PYMEM_ALLOCATOR_MALLOC, 'utf8_mode': 1}
    config = {'use_hash_seed': 1, 'hash_seed': 42, 'tracemalloc': 2, 'import_time': 1, 'malloc_stats': 1, 'inspect': 1, 'optimization_level': 2, 'pythonpath_env': '/my/path', 'pycache_prefix': 'env_pycache_prefix', 'write_bytecode': 0, 'verbose': 1, 'buffered_stdio': 0, 'stdio_encoding': 'iso8859-1', 'stdio_errors': 'replace', 'user_site_directory': 0, 'faulthandler': 1, 'warnoptions': ['EnvVar'], 'platlibdir': 'env_platlibdir', 'module_search_paths': self.IGNORE_CONFIG}
    self.check_all_configs('test_init_python_env', config, preconfig, api=API_PYTHON)
