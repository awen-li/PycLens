# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_netrc.py
# case: NetrcTestCase_test_security

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.temp_cwd(None) as d:
        fn = os.path.join(d, '.netrc')
        with open(fn, 'wt') as f:
            f.write('                    machine foo.domain.com login bar password pass\n                    default login foo password pass\n                    ')
        with os_helper.EnvironmentVarGuard() as environ:
            environ.set('HOME', d)
            os.chmod(fn, 384)
            nrc = netrc.netrc()
            self.assertEqual(nrc.hosts['foo.domain.com'], ('bar', None, 'pass'))
            os.chmod(fn, 402)
            self.assertRaises(netrc.NetrcParseError, netrc.netrc)
