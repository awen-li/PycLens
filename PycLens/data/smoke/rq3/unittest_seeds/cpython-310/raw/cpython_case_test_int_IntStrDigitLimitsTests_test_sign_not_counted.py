# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntStrDigitLimitsTests_test_sign_not_counted

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    int_class = self.int_class
    max_digits = sys.get_int_max_str_digits()
    s = '5' * max_digits
    i = int_class(s)
    pos_i = int_class(f'+{s}')
    assert i == pos_i
    neg_i = int_class(f'-{s}')
    assert -pos_i == neg_i
    str(pos_i)
    str(neg_i)
