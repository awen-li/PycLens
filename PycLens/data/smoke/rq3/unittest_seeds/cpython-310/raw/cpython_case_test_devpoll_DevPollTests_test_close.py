# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_devpoll.py
# case: DevPollTests_test_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    open_file = open(__file__, 'rb')
    self.addCleanup(open_file.close)
    fd = open_file.fileno()
    devpoll = select.devpoll()
    self.assertIsInstance(devpoll.fileno(), int)
    self.assertFalse(devpoll.closed)
    devpoll.close()
    self.assertTrue(devpoll.closed)
    self.assertRaises(ValueError, devpoll.fileno)
    devpoll.close()
    self.assertRaises(ValueError, devpoll.modify, fd, select.POLLIN)
    self.assertRaises(ValueError, devpoll.poll)
    self.assertRaises(ValueError, devpoll.register, fd, select.POLLIN)
    self.assertRaises(ValueError, devpoll.unregister, fd)
