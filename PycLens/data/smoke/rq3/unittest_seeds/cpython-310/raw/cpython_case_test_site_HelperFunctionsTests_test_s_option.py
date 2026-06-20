# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_s_option

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    usersite = os.path.normpath(site.USER_SITE)
    self.assertIn(usersite, sys.path)
    env = os.environ.copy()
    rc = subprocess.call([sys.executable, '-c', 'import sys; sys.exit(%r in sys.path)' % usersite], env=env)
    self.assertEqual(rc, 1)
    env = os.environ.copy()
    rc = subprocess.call([sys.executable, '-s', '-c', 'import sys; sys.exit(%r in sys.path)' % usersite], env=env)
    if usersite == site.getsitepackages()[0]:
        self.assertEqual(rc, 1)
    else:
        self.assertEqual(rc, 0, 'User site still added to path with -s')
    env = os.environ.copy()
    env['PYTHONNOUSERSITE'] = '1'
    rc = subprocess.call([sys.executable, '-c', 'import sys; sys.exit(%r in sys.path)' % usersite], env=env)
    if usersite == site.getsitepackages()[0]:
        self.assertEqual(rc, 1)
    else:
        self.assertEqual(rc, 0, 'User site still added to path with PYTHONNOUSERSITE')
    env = os.environ.copy()
    env['PYTHONUSERBASE'] = '/tmp'
    rc = subprocess.call([sys.executable, '-c', 'import sys, site; sys.exit(site.USER_BASE.startswith("/tmp"))'], env=env)
    self.assertEqual(rc, 1, 'User base not set by PYTHONUSERBASE')
