# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_devpoll.py
# case: DevPollTests_test_timeout_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pollster = select.devpoll()
    (w, r) = os.pipe()
    pollster.register(w)
    pollster.poll(-1)
    self.assertRaises(OverflowError, pollster.poll, -2)
    self.assertRaises(OverflowError, pollster.poll, -1 << 31)
    self.assertRaises(OverflowError, pollster.poll, -1 << 64)
    pollster.poll(0)
    pollster.poll(1)
    pollster.poll(1 << 30)
    self.assertRaises(OverflowError, pollster.poll, 1 << 31)
    self.assertRaises(OverflowError, pollster.poll, 1 << 63)
    self.assertRaises(OverflowError, pollster.poll, 1 << 64)
