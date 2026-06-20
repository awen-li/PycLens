# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_epoll.py
# case: TestEPoll_test_create

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        ep = select.epoll(16)
    except OSError as e:
        raise AssertionError(str(e))
    self.assertTrue(ep.fileno() > 0, ep.fileno())
    self.assertTrue(not ep.closed)
    ep.close()
    self.assertTrue(ep.closed)
    self.assertRaises(ValueError, ep.fileno)
    if hasattr(select, 'EPOLL_CLOEXEC'):
        select.epoll(-1, select.EPOLL_CLOEXEC).close()
        select.epoll(flags=select.EPOLL_CLOEXEC).close()
        select.epoll(flags=0).close()
