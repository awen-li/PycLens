# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: GetpassGetuserTest_test_username_falls_back_to_pwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_name = 'some_name'
    environ.get.return_value = None
    if pwd:
        with mock.patch('os.getuid') as uid, mock.patch('pwd.getpwuid') as getpw:
            uid.return_value = 42
            getpw.return_value = [expected_name]
            self.assertEqual(expected_name, getpass.getuser())
            getpw.assert_called_once_with(42)
    else:
        self.assertRaises(ImportError, getpass.getuser)
