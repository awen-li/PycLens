# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getpass.py
# case: UnixGetpassTest_test_flushes_stream_after_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch('os.open') as open, mock.patch('io.FileIO'), mock.patch('io.TextIOWrapper'), mock.patch('termios.tcgetattr'), mock.patch('termios.tcsetattr'):
        open.return_value = 3
        mock_stream = mock.Mock(spec=StringIO)
        getpass.unix_getpass(stream=mock_stream)
        mock_stream.flush.assert_called_with()
