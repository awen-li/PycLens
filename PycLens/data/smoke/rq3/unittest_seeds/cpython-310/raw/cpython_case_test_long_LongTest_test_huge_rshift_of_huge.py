# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_huge_rshift_of_huge

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    huge = (1 << 500) + 11 << sys.maxsize
    self.assertEqual(huge >> sys.maxsize + 1, (1 << 499) + 5)
    self.assertEqual(huge >> sys.maxsize + 1000, 0)
