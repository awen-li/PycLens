# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_lshift_of_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(0 << 0, 0)
    self.assertEqual(0 << 10, 0)
    with self.assertRaises(ValueError):
        0 << -1
    self.assertEqual(0 << (1 << 1000), 0)
    with self.assertRaises(ValueError):
        0 << -(1 << 1000)
