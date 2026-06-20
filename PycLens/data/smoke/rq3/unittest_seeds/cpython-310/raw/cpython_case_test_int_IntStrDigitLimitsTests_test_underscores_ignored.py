# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntStrDigitLimitsTests_test_underscores_ignored

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    maxdigits = sys.get_int_max_str_digits()
    triples = maxdigits // 3
    s = '111' * triples
    s_ = '1_11' * triples
    self.int_class(s)
    self.int_class(s_)
    self.check(f'{s}111')
    self.check(f'{s_}_111')
