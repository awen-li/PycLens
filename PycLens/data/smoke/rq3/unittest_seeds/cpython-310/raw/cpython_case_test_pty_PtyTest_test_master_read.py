# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pty.py
# case: PtyTest_test_master_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    debug('Calling pty.openpty()')
    (master_fd, slave_fd) = pty.openpty()
    debug(f"Got master_fd '{master_fd}', slave_fd '{slave_fd}'")
    self.addCleanup(os.close, master_fd)
    debug('Closing slave_fd')
    os.close(slave_fd)
    debug('Reading from master_fd')
    try:
        data = os.read(master_fd, 1)
    except OSError:
        data = b''
    self.assertEqual(data, b'')
