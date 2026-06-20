# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_expanduser_home_envvar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.EnvironmentVarGuard() as env:
        env['HOME'] = '/home/victor'
        self.assertEqual(posixpath.expanduser('~'), '/home/victor')
        env['HOME'] = '/home/victor/'
        self.assertEqual(posixpath.expanduser('~'), '/home/victor')
        for home in ('/', '', '//', '///'):
            with self.subTest(home=home):
                env['HOME'] = home
                self.assertEqual(posixpath.expanduser('~'), '/')
                self.assertEqual(posixpath.expanduser('~/'), '/')
                self.assertEqual(posixpath.expanduser('~/foo'), '/foo')
