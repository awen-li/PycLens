# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_uname_win32_ARCHITEW6432

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with os_helper.EnvironmentVarGuard() as environ:
            if 'PROCESSOR_ARCHITEW6432' in environ:
                del environ['PROCESSOR_ARCHITEW6432']
            environ['PROCESSOR_ARCHITECTURE'] = 'foo'
            platform._uname_cache = None
            (system, node, release, version, machine, processor) = platform.uname()
            self.assertEqual(machine, 'foo')
            environ['PROCESSOR_ARCHITEW6432'] = 'bar'
            platform._uname_cache = None
            (system, node, release, version, machine, processor) = platform.uname()
            self.assertEqual(machine, 'bar')
    finally:
        platform._uname_cache = None
