# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_netrc.py
# case: NetrcTestCase_test_home_not_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_cwd(None) as fake_home:
        fake_netrc_path = os.path.join(fake_home, '.netrc')
        with open(fake_netrc_path, 'w') as f:
            f.write('machine foo.domain.com login bar password pass')
        os.chmod(fake_netrc_path, 384)
        orig_expanduser = os.path.expanduser
        called = []

        def fake_expanduser(s):
            called.append(s)
            with os_helper.EnvironmentVarGuard() as environ:
                environ.set('HOME', fake_home)
                environ.set('USERPROFILE', fake_home)
                result = orig_expanduser(s)
                return result
        with support.swap_attr(os.path, 'expanduser', fake_expanduser):
            nrc = netrc.netrc()
            (login, account, password) = nrc.authenticators('foo.domain.com')
            self.assertEqual(login, 'bar')
        self.assertTrue(called)
