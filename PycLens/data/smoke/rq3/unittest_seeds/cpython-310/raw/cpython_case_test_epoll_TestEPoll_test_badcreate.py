# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_epoll.py
# case: TestEPoll_test_badcreate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, select.epoll, 1, 2, 3)
    self.assertRaises(TypeError, select.epoll, 'foo')
    self.assertRaises(TypeError, select.epoll, None)
    self.assertRaises(TypeError, select.epoll, ())
    self.assertRaises(TypeError, select.epoll, ['foo'])
    self.assertRaises(TypeError, select.epoll, {})
    self.assertRaises(ValueError, select.epoll, 0)
    self.assertRaises(ValueError, select.epoll, -2)
    self.assertRaises(ValueError, select.epoll, sizehint=-2)
    if hasattr(select, 'EPOLL_CLOEXEC'):
        self.assertRaises(OSError, select.epoll, flags=12356)
