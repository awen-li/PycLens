# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pwd.py
# case: PwdTest_test_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    entries = pwd.getpwall()
    for e in entries:
        self.assertEqual(len(e), 7)
        self.assertEqual(e[0], e.pw_name)
        self.assertIsInstance(e.pw_name, str)
        self.assertEqual(e[1], e.pw_passwd)
        self.assertIsInstance(e.pw_passwd, str)
        self.assertEqual(e[2], e.pw_uid)
        self.assertIsInstance(e.pw_uid, int)
        self.assertEqual(e[3], e.pw_gid)
        self.assertIsInstance(e.pw_gid, int)
        self.assertEqual(e[4], e.pw_gecos)
        self.assertIn(type(e.pw_gecos), (str, type(None)))
        self.assertEqual(e[5], e.pw_dir)
        self.assertIsInstance(e.pw_dir, str)
        self.assertEqual(e[6], e.pw_shell)
        self.assertIsInstance(e.pw_shell, str)
