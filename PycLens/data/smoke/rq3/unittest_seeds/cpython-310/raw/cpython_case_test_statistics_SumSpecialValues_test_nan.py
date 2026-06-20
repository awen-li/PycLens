# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: SumSpecialValues_test_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for type_ in (float, Decimal):
        nan = type_('nan')
        result = statistics._sum([1, nan, 2])[1]
        self.assertIs(type(result), type_)
        self.assertTrue(math.isnan(result))
