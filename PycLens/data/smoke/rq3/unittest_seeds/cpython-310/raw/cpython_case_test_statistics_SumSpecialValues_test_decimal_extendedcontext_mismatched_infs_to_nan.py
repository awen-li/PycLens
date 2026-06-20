# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: SumSpecialValues_test_decimal_extendedcontext_mismatched_infs_to_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    inf = Decimal('inf')
    data = [1, 2, inf, 3, -inf, 4]
    with decimal.localcontext(decimal.ExtendedContext):
        self.assertTrue(math.isnan(statistics._sum(data)[1]))
