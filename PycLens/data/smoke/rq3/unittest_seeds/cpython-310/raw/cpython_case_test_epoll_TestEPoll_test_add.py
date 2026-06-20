# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_epoll.py
# case: TestEPoll_test_add

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (server, client) = self._connected_pair()
    ep = select.epoll(2)
    try:
        ep.register(server.fileno(), select.EPOLLIN | select.EPOLLOUT)
        ep.register(client.fileno(), select.EPOLLIN | select.EPOLLOUT)
    finally:
        ep.close()
    ep = select.epoll(2)
    try:
        ep.register(server, select.EPOLLIN | select.EPOLLOUT)
        ep.register(client, select.EPOLLIN | select.EPOLLOUT)
    finally:
        ep.close()
    ep = select.epoll(2)
    try:
        self.assertRaises(TypeError, ep.register, object(), select.EPOLLIN | select.EPOLLOUT)
        self.assertRaises(TypeError, ep.register, None, select.EPOLLIN | select.EPOLLOUT)
        self.assertRaises(ValueError, ep.register, -1, select.EPOLLIN | select.EPOLLOUT)
        self.assertRaises(OSError, ep.register, 10000, select.EPOLLIN | select.EPOLLOUT)
        ep.register(server, select.EPOLLIN | select.EPOLLOUT)
        self.assertRaises(OSError, ep.register, server, select.EPOLLIN | select.EPOLLOUT)
    finally:
        ep.close()
