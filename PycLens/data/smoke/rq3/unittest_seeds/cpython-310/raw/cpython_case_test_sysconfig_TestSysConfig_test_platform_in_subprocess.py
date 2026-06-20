# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_platform_in_subprocess

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    my_platform = sysconfig.get_platform()
    env = os.environ.copy()
    if 'MACOSX_DEPLOYMENT_TARGET' in env:
        del env['MACOSX_DEPLOYMENT_TARGET']
    p = subprocess.Popen([sys.executable, '-c', 'import sysconfig; print(sysconfig.get_platform())'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, env=env)
    test_platform = p.communicate()[0].strip()
    test_platform = test_platform.decode('utf-8')
    status = p.wait()
    self.assertEqual(status, 0)
    self.assertEqual(my_platform, test_platform)
    env = os.environ.copy()
    env['MACOSX_DEPLOYMENT_TARGET'] = '10.1'
    p = subprocess.Popen([sys.executable, '-c', 'import sysconfig; print(sysconfig.get_platform())'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, env=env)
    test_platform = p.communicate()[0].strip()
    test_platform = test_platform.decode('utf-8')
    status = p.wait()
    self.assertEqual(status, 0)
    self.assertEqual(my_platform, test_platform)
