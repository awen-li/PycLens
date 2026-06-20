# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualSpecialsTest_test_inf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for type_ in (float, Decimal):
        inf = type_('inf')
        self.assertTrue(approx_equal(inf, inf))
        self.assertTrue(approx_equal(inf, inf, 0, 0))
        self.assertTrue(approx_equal(inf, inf, 1, 0.01))
        self.assertTrue(approx_equal(-inf, -inf))
        self.assertFalse(approx_equal(inf, -inf))
        self.assertFalse(approx_equal(inf, 1000))
