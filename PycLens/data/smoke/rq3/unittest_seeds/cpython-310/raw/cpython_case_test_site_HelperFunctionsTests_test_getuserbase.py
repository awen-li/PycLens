# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_getuserbase

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    site.USER_BASE = None
    user_base = site.getuserbase()
    self.assertEqual(site.USER_BASE, user_base)
    site.USER_BASE = None
    import sysconfig
    sysconfig._CONFIG_VARS = None
    with EnvironmentVarGuard() as environ:
        environ['PYTHONUSERBASE'] = 'xoxo'
        self.assertTrue(site.getuserbase().startswith('xoxo'), site.getuserbase())
