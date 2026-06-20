# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_copy_and_deepcopy_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d = Decimal('43.24')
    c = copy.copy(d)
    self.assertEqual(id(c), id(d))
    dc = copy.deepcopy(d)
    self.assertEqual(id(dc), id(d))
