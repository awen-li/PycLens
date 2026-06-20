# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_epoll.py
# case: TestEPoll_test_control_and_wait

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client, server) = self._connected_pair()
    ep = select.epoll(16)
    ep.register(server.fileno(), select.EPOLLIN | select.EPOLLOUT | select.EPOLLET)
    ep.register(client.fileno(), select.EPOLLIN | select.EPOLLOUT | select.EPOLLET)
    now = time.monotonic()
    events = ep.poll(1, 4)
    then = time.monotonic()
    self.assertFalse(then - now > 0.1, then - now)
    expected = [(client.fileno(), select.EPOLLOUT), (server.fileno(), select.EPOLLOUT)]
    self.assertEqual(sorted(events), sorted(expected))
    events = ep.poll(timeout=0.1, maxevents=4)
    self.assertFalse(events)
    client.sendall(b'Hello!')
    server.sendall(b'world!!!')
    now = time.monotonic()
    events = ep.poll(1.0, 4)
    then = time.monotonic()
    self.assertFalse(then - now > 0.01)
    expected = [(client.fileno(), select.EPOLLIN | select.EPOLLOUT), (server.fileno(), select.EPOLLIN | select.EPOLLOUT)]
    self.assertEqual(sorted(events), sorted(expected))
    ep.unregister(client.fileno())
    ep.modify(server.fileno(), select.EPOLLOUT)
    now = time.monotonic()
    events = ep.poll(1, 4)
    then = time.monotonic()
    self.assertFalse(then - now > 0.01)
    expected = [(server.fileno(), select.EPOLLOUT)]
    self.assertEqual(events, expected)
