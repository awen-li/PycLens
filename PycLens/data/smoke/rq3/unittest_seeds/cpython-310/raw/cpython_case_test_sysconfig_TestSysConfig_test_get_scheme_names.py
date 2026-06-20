# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_get_scheme_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    wanted = ['nt', 'posix_home', 'posix_prefix']
    if HAS_USER_BASE:
        wanted.extend(['nt_user', 'osx_framework_user', 'posix_user'])
    self.assertEqual(get_scheme_names(), tuple(sorted(wanted)))
