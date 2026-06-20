# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_repeat_with_negative_times

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(repeat('a', -1)), "repeat('a', 0)")
    self.assertEqual(repr(repeat('a', -2)), "repeat('a', 0)")
    self.assertEqual(repr(repeat('a', times=-1)), "repeat('a', 0)")
    self.assertEqual(repr(repeat('a', times=-2)), "repeat('a', 0)")
