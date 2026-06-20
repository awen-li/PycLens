# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_pybuilddir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.tmpdir_with_python() as tmpdir:
        subdir = 'libdir'
        libdir = os.path.join(tmpdir, subdir)
        os.mkdir(libdir)
        filename = os.path.join(tmpdir, 'pybuilddir.txt')
        with open(filename, 'w', encoding='utf8') as fp:
            fp.write(subdir)
        module_search_paths = self.module_search_paths()
        module_search_paths[-1] = libdir
        executable = self.test_exe
        config = {'base_executable': executable, 'executable': executable, 'module_search_paths': module_search_paths}
        env = self.copy_paths_by_env(config)
        self.check_all_configs('test_init_compat_config', config, api=API_COMPAT, env=env, ignore_stderr=True, cwd=tmpdir)
