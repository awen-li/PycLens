# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_initgroups

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, posix.initgroups)
    self.assertRaises(TypeError, posix.initgroups, None)
    self.assertRaises(TypeError, posix.initgroups, 3, 'foo')
    self.assertRaises(TypeError, posix.initgroups, 'foo', 3, object())
    if os.getuid() != 0:
        try:
            name = pwd.getpwuid(posix.getuid()).pw_name
        except KeyError:
            raise unittest.SkipTest('need a pwd entry')
        try:
            posix.initgroups(name, 13)
        except OSError as e:
            self.assertEqual(e.errno, errno.EPERM)
        else:
            self.fail('Expected OSError to be raised by initgroups')
