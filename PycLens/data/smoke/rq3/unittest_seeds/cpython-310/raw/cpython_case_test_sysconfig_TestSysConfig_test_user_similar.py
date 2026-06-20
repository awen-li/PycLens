# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_user_similar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = get_config_var('base')
    if HAS_USER_BASE:
        user = get_config_var('userbase')
    adapt = sys.base_prefix != sys.base_exec_prefix
    for name in ('stdlib', 'platstdlib', 'purelib', 'platlib'):
        global_path = get_path(name, 'posix_prefix')
        if adapt:
            global_path = global_path.replace(sys.exec_prefix, sys.base_prefix)
            base = base.replace(sys.exec_prefix, sys.base_prefix)
        elif sys.base_prefix != sys.prefix:
            global_path = global_path.replace(sys.base_prefix, sys.prefix)
            base = base.replace(sys.base_prefix, sys.prefix)
        if HAS_USER_BASE:
            user_path = get_path(name, 'posix_user')
            expected = os.path.normpath(global_path.replace(base, user, 1))
            if name == 'platlib':
                py_version_short = sysconfig.get_python_version()
                suffix = f'python{py_version_short}/site-packages'
                expected = expected.replace(f'/{sys.platlibdir}/{suffix}', f'/lib/{suffix}')
            self.assertEqual(user_path, expected)
