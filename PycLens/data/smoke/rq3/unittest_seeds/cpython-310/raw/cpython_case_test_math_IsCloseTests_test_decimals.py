# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: IsCloseTests_test_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from decimal import Decimal
    decimal_examples = [(Decimal('1.00000001'), Decimal('1.0')), (Decimal('1.00000001e-20'), Decimal('1.0e-20')), (Decimal('1.00000001e-100'), Decimal('1.0e-100')), (Decimal('1.00000001e20'), Decimal('1.0e20'))]
    self.assertAllClose(decimal_examples, rel_tol=1e-08)
    self.assertAllNotClose(decimal_examples, rel_tol=1e-09)
