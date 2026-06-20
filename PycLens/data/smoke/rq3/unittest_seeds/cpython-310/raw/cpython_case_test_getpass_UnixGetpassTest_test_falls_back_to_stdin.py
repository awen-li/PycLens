# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: UnixGetpassTest_test_falls_back_to_stdin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch('os.open') as os_open, mock.patch('sys.stdin', spec=StringIO) as stdin:
        os_open.side_effect = IOError
        stdin.fileno.side_effect = AttributeError
        with support.captured_stderr() as stderr:
            with self.assertWarns(getpass.GetPassWarning):
                getpass.unix_getpass()
        stdin.readline.assert_called_once_with()
        self.assertIn('Warning', stderr.getvalue())
        self.assertIn('Password:', stderr.getvalue())
