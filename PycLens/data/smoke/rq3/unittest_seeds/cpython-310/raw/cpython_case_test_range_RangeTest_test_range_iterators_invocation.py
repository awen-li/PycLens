# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_range_iterators_invocation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rangeiter_type = type(iter(range(0)))
    self.assertRaises(TypeError, rangeiter_type, 1, 3, 1)
    long_rangeiter_type = type(iter(range(1 << 1000)))
    self.assertRaises(TypeError, long_rangeiter_type, 1, 3, 1)
