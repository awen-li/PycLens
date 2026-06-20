# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_floordiv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ZeroDivisionError):
        _ = 1 // 0
    self.assertEqual(2 // 3, 0)
    self.assertEqual(2 // -3, -1)
    self.assertEqual(-2 // 3, -1)
    self.assertEqual(-2 // -3, 0)
    self.assertEqual(-11 // -3, 3)
    self.assertEqual(-11 // 3, -4)
    self.assertEqual(11 // -3, -4)
    self.assertEqual(11 // 3, 3)
    self.assertEqual(-12 // -3, 4)
    self.assertEqual(-12 // 3, -4)
    self.assertEqual(12 // -3, -4)
    self.assertEqual(12 // 3, 4)
