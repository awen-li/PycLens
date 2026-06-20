# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_epoll.py
# case: TestEPoll_test_unregister_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (server, client) = self._connected_pair()
    fd = server.fileno()
    ep = select.epoll(16)
    ep.register(server)
    now = time.monotonic()
    events = ep.poll(1, 4)
    then = time.monotonic()
    self.assertFalse(then - now > 0.01)
    server.close()
    with self.assertRaises(OSError) as cm:
        ep.unregister(fd)
    self.assertEqual(cm.exception.errno, errno.EBADF)
