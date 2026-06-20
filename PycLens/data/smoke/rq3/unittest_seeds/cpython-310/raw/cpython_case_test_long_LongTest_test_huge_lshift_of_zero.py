# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_huge_lshift_of_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(0 << sys.maxsize, 0)
    self.assertEqual(0 << sys.maxsize + 1, 0)
