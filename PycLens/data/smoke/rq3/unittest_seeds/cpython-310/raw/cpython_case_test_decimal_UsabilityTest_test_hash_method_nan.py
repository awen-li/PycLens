# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_hash_method_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    self.assertRaises(TypeError, hash, Decimal('sNaN'))
    value = Decimal('NaN')
    self.assertEqual(hash(value), object.__hash__(value))

    class H:

        def __hash__(self):
            return 42

    class D(Decimal, H):
        pass
    value = D('NaN')
    self.assertEqual(hash(value), object.__hash__(value))
