# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PosixPathTest_test_expanduser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    import_helper.import_module('pwd')
    import pwd
    pwdent = pwd.getpwuid(os.getuid())
    username = pwdent.pw_name
    userhome = pwdent.pw_dir.rstrip('/') or '/'
    for pwdent in pwd.getpwall():
        othername = pwdent.pw_name
        otherhome = pwdent.pw_dir.rstrip('/')
        if othername != username and otherhome:
            break
    else:
        othername = username
        otherhome = userhome
    fakename = 'fakeuser'
    try:
        while pwd.getpwnam(fakename):
            fakename += '1'
    except KeyError:
        pass
    p1 = P('~/Documents')
    p2 = P(f'~{username}/Documents')
    p3 = P(f'~{othername}/Documents')
    p4 = P(f'../~{username}/Documents')
    p5 = P(f'/~{username}/Documents')
    p6 = P('')
    p7 = P(f'~{fakename}/Documents')
    with os_helper.EnvironmentVarGuard() as env:
        env.pop('HOME', None)
        self.assertEqual(p1.expanduser(), P(userhome) / 'Documents')
        self.assertEqual(p2.expanduser(), P(userhome) / 'Documents')
        self.assertEqual(p3.expanduser(), P(otherhome) / 'Documents')
        self.assertEqual(p4.expanduser(), p4)
        self.assertEqual(p5.expanduser(), p5)
        self.assertEqual(p6.expanduser(), p6)
        self.assertRaises(RuntimeError, p7.expanduser)
        env['HOME'] = '/tmp'
        self.assertEqual(p1.expanduser(), P('/tmp/Documents'))
        self.assertEqual(p2.expanduser(), P(userhome) / 'Documents')
        self.assertEqual(p3.expanduser(), P(otherhome) / 'Documents')
        self.assertEqual(p4.expanduser(), p4)
        self.assertEqual(p5.expanduser(), p5)
        self.assertEqual(p6.expanduser(), p6)
        self.assertRaises(RuntimeError, p7.expanduser)
