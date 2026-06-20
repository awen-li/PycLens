# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: UnixGetpassTest_test_falls_back_to_fallback_if_termios_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch('os.open') as open, mock.patch('io.FileIO') as fileio, mock.patch('io.TextIOWrapper') as textio, mock.patch('termios.tcgetattr'), mock.patch('termios.tcsetattr') as tcsetattr, mock.patch('getpass.fallback_getpass') as fallback:
        open.return_value = 3
        fileio.return_value = BytesIO()
        tcsetattr.side_effect = termios.error
        getpass.unix_getpass()
        fallback.assert_called_once_with('Password: ', textio.return_value)
