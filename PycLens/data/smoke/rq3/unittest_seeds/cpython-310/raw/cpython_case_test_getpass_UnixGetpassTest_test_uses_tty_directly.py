# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: UnixGetpassTest_test_uses_tty_directly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch('os.open') as open, mock.patch('io.FileIO') as fileio, mock.patch('io.TextIOWrapper') as textio:
        open.return_value = None
        getpass.unix_getpass()
        open.assert_called_once_with('/dev/tty', os.O_RDWR | os.O_NOCTTY)
        fileio.assert_called_once_with(open.return_value, 'w+')
        textio.assert_called_once_with(fileio.return_value)
