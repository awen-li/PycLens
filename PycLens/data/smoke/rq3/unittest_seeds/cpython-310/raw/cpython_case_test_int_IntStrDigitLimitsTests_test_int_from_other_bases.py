# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntStrDigitLimitsTests_test_int_from_other_bases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = 3
    with self.subTest(base=base):
        self._other_base_helper(base)
    base = 36
    with self.subTest(base=base):
        self._other_base_helper(base)
