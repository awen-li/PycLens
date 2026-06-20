# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_negative_shift_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        42 << -3
    with self.assertRaises(ValueError):
        42 << -(1 << 1000)
    with self.assertRaises(ValueError):
        42 >> -3
    with self.assertRaises(ValueError):
        42 >> -(1 << 1000)
