# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_devpoll.py
# case: DevPollTests_test_events_mask_overflow_c_limits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import USHRT_MAX
    pollster = select.devpoll()
    (w, r) = os.pipe()
    pollster.register(w)
    self.assertRaises(OverflowError, pollster.register, 0, USHRT_MAX + 1)
    self.assertRaises(OverflowError, pollster.modify, 1, USHRT_MAX + 1)
