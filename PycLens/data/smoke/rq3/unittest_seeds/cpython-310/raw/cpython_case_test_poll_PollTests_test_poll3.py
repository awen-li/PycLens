# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poll.py
# case: PollTests_test_poll3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pollster = select.poll()
    pollster.register(1)
    self.assertRaises(OverflowError, pollster.poll, 1 << 64)
    x = 2 + 3
    if x != 5:
        self.fail('Overflow must have occurred')
    self.assertRaises(ValueError, pollster.register, 0, -1)
    self.assertRaises(OverflowError, pollster.register, 0, 1 << 64)
    self.assertRaises(ValueError, pollster.modify, 1, -1)
    self.assertRaises(OverflowError, pollster.modify, 1, 1 << 64)
