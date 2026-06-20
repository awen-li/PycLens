# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: AverageMixin_test_single_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (23, 42.5, 1300000000000000.0, Fraction(15, 19), Decimal('0.28')):
        self.assertEqual(self.func([x]), x)
