# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: WindowsPathTest_test_expanduser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    with os_helper.EnvironmentVarGuard() as env:
        env.pop('HOME', None)
        env.pop('USERPROFILE', None)
        env.pop('HOMEPATH', None)
        env.pop('HOMEDRIVE', None)
        env['USERNAME'] = 'alice'
        p1 = P('~/My Documents')
        p2 = P('~alice/My Documents')
        p3 = P('~bob/My Documents')
        p4 = P('/~/My Documents')
        p5 = P('d:~/My Documents')
        p6 = P('')
        self.assertRaises(RuntimeError, p1.expanduser)
        self.assertRaises(RuntimeError, p2.expanduser)
        self.assertRaises(RuntimeError, p3.expanduser)
        self.assertEqual(p4.expanduser(), p4)
        self.assertEqual(p5.expanduser(), p5)
        self.assertEqual(p6.expanduser(), p6)

        def check():
            env.pop('USERNAME', None)
            self.assertEqual(p1.expanduser(), P('C:/Users/alice/My Documents'))
            self.assertRaises(RuntimeError, p2.expanduser)
            env['USERNAME'] = 'alice'
            self.assertEqual(p2.expanduser(), P('C:/Users/alice/My Documents'))
            self.assertEqual(p3.expanduser(), P('C:/Users/bob/My Documents'))
            self.assertEqual(p4.expanduser(), p4)
            self.assertEqual(p5.expanduser(), p5)
            self.assertEqual(p6.expanduser(), p6)
        env['HOMEPATH'] = 'C:\\Users\\alice'
        check()
        env['HOMEDRIVE'] = 'C:\\'
        env['HOMEPATH'] = 'Users\\alice'
        check()
        env.pop('HOMEDRIVE', None)
        env.pop('HOMEPATH', None)
        env['USERPROFILE'] = 'C:\\Users\\alice'
        check()
        env['HOME'] = 'C:\\Users\\eve'
        check()
