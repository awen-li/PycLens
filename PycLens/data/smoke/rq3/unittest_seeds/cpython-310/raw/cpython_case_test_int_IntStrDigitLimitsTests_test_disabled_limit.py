# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntStrDigitLimitsTests_test_disabled_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertGreater(sys.get_int_max_str_digits(), 0)
    self.assertLess(sys.get_int_max_str_digits(), 20000)
    with support.adjust_int_max_str_digits(0):
        self.assertEqual(sys.get_int_max_str_digits(), 0)
        i = self.int_class('1' * 20000)
        str(i)
    self.assertGreater(sys.get_int_max_str_digits(), 0)
