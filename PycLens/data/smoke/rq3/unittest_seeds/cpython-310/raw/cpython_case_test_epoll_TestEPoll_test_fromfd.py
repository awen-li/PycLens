# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_epoll.py
# case: TestEPoll_test_fromfd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (server, client) = self._connected_pair()
    with select.epoll(2) as ep:
        ep2 = select.epoll.fromfd(ep.fileno())
        ep2.register(server.fileno(), select.EPOLLIN | select.EPOLLOUT)
        ep2.register(client.fileno(), select.EPOLLIN | select.EPOLLOUT)
        events = ep.poll(1, 4)
        events2 = ep2.poll(0.9, 4)
        self.assertEqual(len(events), 2)
        self.assertEqual(len(events2), 2)
    try:
        ep2.poll(1, 4)
    except OSError as e:
        self.assertEqual(e.args[0], errno.EBADF, e)
    else:
        self.fail("epoll on closed fd didn't raise EBADF")
