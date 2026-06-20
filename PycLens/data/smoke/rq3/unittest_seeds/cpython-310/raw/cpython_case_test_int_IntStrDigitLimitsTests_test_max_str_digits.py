# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntStrDigitLimitsTests_test_max_str_digits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    maxdigits = sys.get_int_max_str_digits()
    self.check('1' * (maxdigits + 1))
    self.check(' ' + '1' * (maxdigits + 1))
    self.check('1' * (maxdigits + 1) + ' ')
    self.check('+' + '1' * (maxdigits + 1))
    self.check('-' + '1' * (maxdigits + 1))
    self.check('1' * (maxdigits + 1))
    i = 10 ** maxdigits
    with self.assertRaises(ValueError):
        str(i)
