# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_devpoll.py
# case: DevPollTests_test_fd_non_inheritable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    devpoll = select.devpoll()
    self.addCleanup(devpoll.close)
    self.assertEqual(os.get_inheritable(devpoll.fileno()), False)
