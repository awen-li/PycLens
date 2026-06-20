# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ExactRatioTest_test_decimal_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NAN = Decimal('NAN')
    sNAN = Decimal('sNAN')

    class MyDecimal(Decimal):
        pass
    for nan in (NAN, MyDecimal(NAN), sNAN, MyDecimal(sNAN)):
        ratio = statistics._exact_ratio(nan)
        self.assertTrue(_nan_equal(ratio[0], nan))
        self.assertIs(ratio[1], None)
        self.assertEqual(type(ratio[0]), type(nan))
