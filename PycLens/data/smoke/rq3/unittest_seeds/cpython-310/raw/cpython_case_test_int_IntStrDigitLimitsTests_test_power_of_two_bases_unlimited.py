# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntStrDigitLimitsTests_test_power_of_two_bases_unlimited

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    maxdigits = sys.get_int_max_str_digits()
    for base in (2, 4, 8, 16, 32):
        with self.subTest(base=base):
            self.int_class('1' * (maxdigits + 1), base)
            assert maxdigits < 100000
            self.int_class('1' * 100000, base)
