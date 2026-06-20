# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: InitConfigTests_test_init_pyvenv_cfg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.tmpdir_with_python() as tmpdir, tempfile.TemporaryDirectory() as pyvenv_home:
        ver = sys.version_info
        if not MS_WINDOWS:
            lib_dynload = os.path.join(pyvenv_home, sys.platlibdir, f'python{ver.major}.{ver.minor}', 'lib-dynload')
            os.makedirs(lib_dynload)
        else:
            lib_dynload = os.path.join(pyvenv_home, 'lib')
            os.makedirs(lib_dynload)
            shutil.copyfile(os.__file__, os.path.join(lib_dynload, 'os.py'))
        filename = os.path.join(tmpdir, 'pyvenv.cfg')
        with open(filename, 'w', encoding='utf8') as fp:
            print('home = %s' % pyvenv_home, file=fp)
            print('include-system-site-packages = false', file=fp)
        paths = self.module_search_paths()
        if not MS_WINDOWS:
            paths[-1] = lib_dynload
        else:
            for (index, path) in enumerate(paths):
                if index == 0:
                    paths[index] = os.path.join(tmpdir, os.path.basename(path))
                else:
                    paths[index] = os.path.join(pyvenv_home, os.path.basename(path))
            paths[-1] = pyvenv_home
        executable = self.test_exe
        exec_prefix = pyvenv_home
        config = {'base_exec_prefix': exec_prefix, 'exec_prefix': exec_prefix, 'base_executable': executable, 'executable': executable, 'module_search_paths': paths}
        path_config = {}
        if MS_WINDOWS:
            config['base_prefix'] = pyvenv_home
            config['prefix'] = pyvenv_home
            ver = sys.version_info
            dll = f'python{ver.major}'
            if debug_build(executable):
                dll += '_d'
            dll += '.DLL'
            dll = os.path.join(os.path.dirname(executable), dll)
            path_config['python3_dll'] = dll
        env = self.copy_paths_by_env(config)
        self.check_all_configs('test_init_compat_config', config, expected_pathconfig=path_config, api=API_COMPAT, env=env, ignore_stderr=True, cwd=tmpdir)
