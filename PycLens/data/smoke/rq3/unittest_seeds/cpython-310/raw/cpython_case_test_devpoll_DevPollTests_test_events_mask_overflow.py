# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_devpoll.py
# case: DevPollTests_test_events_mask_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pollster = select.devpoll()
    (w, r) = os.pipe()
    pollster.register(w)
    self.assertRaises(ValueError, pollster.register, 0, -1)
    self.assertRaises(OverflowError, pollster.register, 0, 1 << 64)
    self.assertRaises(ValueError, pollster.modify, 1, -1)
    self.assertRaises(OverflowError, pollster.modify, 1, 1 << 64)
