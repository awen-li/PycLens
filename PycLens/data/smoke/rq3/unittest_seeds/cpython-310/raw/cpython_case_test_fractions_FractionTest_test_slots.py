# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fractions.py
# case: FractionTest_test_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = F(13, 7)
    self.assertRaises(AttributeError, setattr, r, 'a', 10)
