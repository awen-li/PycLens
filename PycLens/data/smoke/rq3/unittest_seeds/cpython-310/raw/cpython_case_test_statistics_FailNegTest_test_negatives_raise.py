# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: FailNegTest_test_negatives_raise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in [1, 2.0, Fraction(3), Decimal(4)]:
        seq = [-x]
        it = statistics._fail_neg(seq)
        self.assertRaises(statistics.StatisticsError, next, it)
