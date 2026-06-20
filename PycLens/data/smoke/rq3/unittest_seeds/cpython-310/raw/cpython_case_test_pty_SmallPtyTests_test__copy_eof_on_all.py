# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pty.py
# case: SmallPtyTests_test__copy_eof_on_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (read_from_stdout_fd, mock_stdout_fd) = self._pipe()
    pty.STDOUT_FILENO = mock_stdout_fd
    (mock_stdin_fd, write_to_stdin_fd) = self._pipe()
    pty.STDIN_FILENO = mock_stdin_fd
    socketpair = self._socketpair()
    masters = [s.fileno() for s in socketpair]
    socketpair[1].close()
    os.close(write_to_stdin_fd)
    pty.select = self._mock_select
    self.select_rfds_lengths.append(2)
    self.select_rfds_results.append([mock_stdin_fd, masters[0]])
    self.select_rfds_lengths.append(0)
    self.assertEqual(pty._copy(masters[0]), None)
