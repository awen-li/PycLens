# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poll.py
# case: PollTests_test_poll_c_limits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import USHRT_MAX, INT_MAX, UINT_MAX
    pollster = select.poll()
    pollster.register(1)
    self.assertRaises(OverflowError, pollster.register, 0, USHRT_MAX + 1)
    self.assertRaises(OverflowError, pollster.modify, 1, USHRT_MAX + 1)
    self.assertRaises(OverflowError, pollster.poll, INT_MAX + 1)
    self.assertRaises(OverflowError, pollster.poll, UINT_MAX + 1)
