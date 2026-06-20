# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_expanduser_pwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pwd = import_helper.import_module('pwd')
    self.assertIsInstance(posixpath.expanduser('~/'), str)
    self.assertIsInstance(posixpath.expanduser(b'~/'), bytes)
    if posixpath.expanduser('~') != '/':
        self.assertEqual(posixpath.expanduser('~') + '/', posixpath.expanduser('~/'))
        self.assertEqual(posixpath.expanduser(b'~') + b'/', posixpath.expanduser(b'~/'))
    self.assertIsInstance(posixpath.expanduser('~root/'), str)
    self.assertIsInstance(posixpath.expanduser('~foo/'), str)
    self.assertIsInstance(posixpath.expanduser(b'~root/'), bytes)
    self.assertIsInstance(posixpath.expanduser(b'~foo/'), bytes)
    with os_helper.EnvironmentVarGuard() as env:
        del env['HOME']
        home = pwd.getpwuid(os.getuid()).pw_dir
        home = home.rstrip('/') or '/'
        self.assertEqual(posixpath.expanduser('~'), home)
        with mock.patch.object(pwd, 'getpwuid', side_effect=KeyError), mock.patch.object(pwd, 'getpwnam', side_effect=KeyError):
            for path in ('~', '~/.local', '~vstinner/'):
                self.assertEqual(posixpath.expanduser(path), path)
