# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntStrDigitLimitsTests_test_max_str_digits_edge_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    int_class = self.int_class
    maxdigits = sys.get_int_max_str_digits()
    int_class('1' * maxdigits)
    int_class(' ' + '1' * maxdigits)
    int_class('1' * maxdigits + ' ')
    int_class('+' + '1' * maxdigits)
    int_class('-' + '1' * maxdigits)
    self.assertEqual(len(str(10 ** (maxdigits - 1))), maxdigits)
