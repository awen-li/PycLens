# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: UnixGetpassTest_test_resets_termios

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch('os.open') as open, mock.patch('io.FileIO'), mock.patch('io.TextIOWrapper'), mock.patch('termios.tcgetattr') as tcgetattr, mock.patch('termios.tcsetattr') as tcsetattr:
        open.return_value = 3
        fake_attrs = [255, 255, 255, 255, 255]
        tcgetattr.return_value = list(fake_attrs)
        getpass.unix_getpass()
        tcsetattr.assert_called_with(3, mock.ANY, fake_attrs)
