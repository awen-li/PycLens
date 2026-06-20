# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_setpath_config

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = self._get_expected_config()
    paths = config['config']['module_search_paths']
    config = {'module_search_paths': paths, 'prefix': '', 'base_prefix': '', 'exec_prefix': '', 'base_exec_prefix': '', 'program_name': 'conf_program_name', 'base_executable': 'conf_executable', 'executable': 'conf_executable'}
    env = {'TESTPATH': os.path.pathsep.join(paths)}
    self.check_all_configs('test_init_setpath_config', config, api=API_PYTHON, env=env, ignore_stderr=True)
