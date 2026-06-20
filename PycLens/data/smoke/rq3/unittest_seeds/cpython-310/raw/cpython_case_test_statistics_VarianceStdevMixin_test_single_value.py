# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: VarianceStdevMixin_test_single_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (11, 19.8, 460000000000000.0, Fraction(21, 34), Decimal('8.392')):
        self.assertEqual(self.func([x]), 0)
