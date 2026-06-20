# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_epoll.py
# case: TestEPoll_test_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    open_file = open(__file__, 'rb')
    self.addCleanup(open_file.close)
    fd = open_file.fileno()
    epoll = select.epoll()
    self.assertIsInstance(epoll.fileno(), int)
    self.assertFalse(epoll.closed)
    epoll.close()
    self.assertTrue(epoll.closed)
    self.assertRaises(ValueError, epoll.fileno)
    epoll.close()
    self.assertRaises(ValueError, epoll.modify, fd, select.EPOLLIN)
    self.assertRaises(ValueError, epoll.poll, 1.0)
    self.assertRaises(ValueError, epoll.register, fd, select.EPOLLIN)
    self.assertRaises(ValueError, epoll.unregister, fd)
