# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: HelperFunctionsTests_test_no_home_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    site.USER_SITE = None
    site.USER_BASE = None
    with EnvironmentVarGuard() as environ, mock.patch('os.path.expanduser', lambda path: path):
        del environ['PYTHONUSERBASE']
        del environ['APPDATA']
        user_base = site.getuserbase()
        self.assertTrue(user_base.startswith('~' + os.sep), user_base)
        user_site = site.getusersitepackages()
        self.assertTrue(user_site.startswith(user_base), user_site)
    with mock.patch('os.path.isdir', return_value=False) as mock_isdir, mock.patch.object(site, 'addsitedir') as mock_addsitedir, support.swap_attr(site, 'ENABLE_USER_SITE', True):
        known_paths = set()
        site.addusersitepackages(known_paths)
        mock_isdir.assert_called_once_with(user_site)
        mock_addsitedir.assert_not_called()
        self.assertFalse(known_paths)
