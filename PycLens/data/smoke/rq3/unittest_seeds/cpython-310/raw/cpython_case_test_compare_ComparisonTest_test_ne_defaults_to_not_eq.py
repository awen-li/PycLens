# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compare.py
# case: ComparisonTest_test_ne_defaults_to_not_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = Cmp(1)
    b = Cmp(1)
    c = Cmp(2)
    self.assertIs(a == b, True)
    self.assertIs(a != b, False)
    self.assertIs(a != c, True)
