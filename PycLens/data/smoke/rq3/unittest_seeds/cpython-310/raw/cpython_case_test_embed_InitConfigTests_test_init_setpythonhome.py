# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_setpythonhome

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = self._get_expected_config()
    paths = config['config']['module_search_paths']
    paths_str = os.path.pathsep.join(paths)
    for path in paths:
        if not os.path.isdir(path):
            continue
        if os.path.exists(os.path.join(path, 'os.py')):
            home = os.path.dirname(path)
            break
    else:
        self.fail(f'Unable to find home in {paths!r}')
    prefix = exec_prefix = home
    expected_paths = self.module_search_paths(prefix=home, exec_prefix=home)
    config = {'home': home, 'module_search_paths': expected_paths, 'prefix': prefix, 'base_prefix': prefix, 'exec_prefix': exec_prefix, 'base_exec_prefix': exec_prefix, 'pythonpath_env': paths_str}
    self.default_program_name(config)
    env = {'TESTHOME': home, 'PYTHONPATH': paths_str}
    self.check_all_configs('test_init_setpythonhome', config, api=API_COMPAT, env=env)
