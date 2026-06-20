# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_mod_division

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ZeroDivisionError):
        _ = 1 % 0
    self.assertEqual(13 % 10, 3)
    self.assertEqual(-13 % 10, 7)
    self.assertEqual(13 % -10, -7)
    self.assertEqual(-13 % -10, -3)
    self.assertEqual(12 % 4, 0)
    self.assertEqual(-12 % 4, 0)
    self.assertEqual(12 % -4, 0)
    self.assertEqual(-12 % -4, 0)
