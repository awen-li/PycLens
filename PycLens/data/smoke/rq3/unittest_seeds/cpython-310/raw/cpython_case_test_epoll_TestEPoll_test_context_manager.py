# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_epoll.py
# case: TestEPoll_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with select.epoll(16) as ep:
        self.assertGreater(ep.fileno(), 0)
        self.assertFalse(ep.closed)
    self.assertTrue(ep.closed)
    self.assertRaises(ValueError, ep.fileno)
