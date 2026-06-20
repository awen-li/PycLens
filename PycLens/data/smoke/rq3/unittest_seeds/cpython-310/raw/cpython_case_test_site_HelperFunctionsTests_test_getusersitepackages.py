# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_getusersitepackages

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    site.USER_SITE = None
    site.USER_BASE = None
    user_site = site.getusersitepackages()
    self.assertEqual(site.USER_SITE, user_site)
    self.assertTrue(user_site.startswith(site.USER_BASE), user_site)
    self.assertEqual(site.USER_BASE, site.getuserbase())
