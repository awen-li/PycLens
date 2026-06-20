# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: _TestMboxMMDF_test_lock_conflict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (c, p) = socket.socketpair()
    self.addCleanup(c.close)
    self.addCleanup(p.close)
    pid = os.fork()
    if pid == 0:
        try:
            self._box.lock()
            c.send(b'c')
            c.recv(1)
            self._box.unlock()
        finally:
            os._exit(0)
    p.recv(1)
    try:
        self.assertRaises(mailbox.ExternalClashError, self._box.lock)
    finally:
        p.send(b'p')
        support.wait_process(pid, exitcode=0)
    self._box.lock()
    self._box.unlock()
