# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pty.py
# case: PtyTest_test_openpty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        mode = tty.tcgetattr(pty.STDIN_FILENO)
    except tty.error:
        debug('tty.tcgetattr(pty.STDIN_FILENO) failed')
        mode = None
    new_stdin_winsz = None
    if self.stdin_rows is not None and self.stdin_cols is not None:
        try:
            debug('Setting pty.STDIN_FILENO window size')
            debug(f'original size: (rows={self.stdin_rows}, cols={self.stdin_cols})')
            target_stdin_rows = self.stdin_rows + 1
            target_stdin_cols = self.stdin_cols + 1
            debug(f'target size: (rows={target_stdin_rows}, cols={target_stdin_cols})')
            target_stdin_winsz = struct.pack('HHHH', target_stdin_rows, target_stdin_cols, 0, 0)
            _set_term_winsz(pty.STDIN_FILENO, target_stdin_winsz)
            new_stdin_winsz = _get_term_winsz(pty.STDIN_FILENO)
            self.assertEqual(new_stdin_winsz, target_stdin_winsz, 'pty.STDIN_FILENO window size unchanged')
        except OSError:
            warnings.warn('Failed to set pty.STDIN_FILENO window size')
            pass
    try:
        debug('Calling pty.openpty()')
        try:
            (master_fd, slave_fd) = pty.openpty(mode, new_stdin_winsz)
        except TypeError:
            (master_fd, slave_fd) = pty.openpty()
        debug(f"Got master_fd '{master_fd}', slave_fd '{slave_fd}'")
    except OSError:
        raise unittest.SkipTest('Pseudo-terminals (seemingly) not functional.')
    self.addCleanup(os.close, master_fd)
    self.addCleanup(os.close, slave_fd)
    self.assertTrue(os.isatty(slave_fd), 'slave_fd is not a tty')
    if mode:
        self.assertEqual(tty.tcgetattr(slave_fd), mode, 'openpty() failed to set slave termios')
    if new_stdin_winsz:
        self.assertEqual(_get_term_winsz(slave_fd), new_stdin_winsz, 'openpty() failed to set slave window size')
    blocking = os.get_blocking(master_fd)
    try:
        os.set_blocking(master_fd, False)
        try:
            s1 = os.read(master_fd, 1024)
            self.assertEqual(b'', s1)
        except OSError as e:
            if e.errno != errno.EAGAIN:
                raise
    finally:
        os.set_blocking(master_fd, blocking)
    debug('Writing to slave_fd')
    os.write(slave_fd, TEST_STRING_1)
    s1 = _readline(master_fd)
    self.assertEqual(b'I wish to buy a fish license.\n', normalize_output(s1))
    debug('Writing chunked output')
    os.write(slave_fd, TEST_STRING_2[:5])
    os.write(slave_fd, TEST_STRING_2[5:])
    s2 = _readline(master_fd)
    self.assertEqual(b'For my pet fish, Eric.\n', normalize_output(s2))
