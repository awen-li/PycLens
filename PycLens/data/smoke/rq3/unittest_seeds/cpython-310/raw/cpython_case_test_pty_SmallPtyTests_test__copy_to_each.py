# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pty.py
# case: SmallPtyTests_test__copy_to_each

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (read_from_stdout_fd, mock_stdout_fd) = self._pipe()
    pty.STDOUT_FILENO = mock_stdout_fd
    (mock_stdin_fd, write_to_stdin_fd) = self._pipe()
    pty.STDIN_FILENO = mock_stdin_fd
    socketpair = self._socketpair()
    masters = [s.fileno() for s in socketpair]
    os.write(masters[1], b'from master')
    os.write(write_to_stdin_fd, b'from stdin')
    pty.select = self._mock_select
    self.select_rfds_lengths.append(2)
    self.select_rfds_results.append([mock_stdin_fd, masters[0]])
    self.select_rfds_lengths.append(2)
    with self.assertRaises(IndexError):
        pty._copy(masters[0])
    rfds = select.select([read_from_stdout_fd, masters[1]], [], [], 0)[0]
    self.assertEqual([read_from_stdout_fd, masters[1]], rfds)
    self.assertEqual(os.read(read_from_stdout_fd, 20), b'from master')
    self.assertEqual(os.read(masters[1], 20), b'from stdin')
