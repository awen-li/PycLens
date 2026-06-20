# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_get_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.platform == 'darwin' and sys._framework:
        scheme = 'osx_framework_user'
    else:
        scheme = os.name + '_user'
    self.assertEqual(os.path.normpath(site._get_path(site._getuserbase())), sysconfig.get_path('purelib', scheme))
