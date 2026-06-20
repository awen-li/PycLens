# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PythonAPItests_test_complex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    x = Decimal('9.8182731e181273')
    self.assertEqual(x.real, x)
    self.assertEqual(x.imag, 0)
    self.assertEqual(x.conjugate(), x)
    x = Decimal('1')
    self.assertEqual(complex(x), complex(float(1)))
    self.assertRaises(AttributeError, setattr, x, 'real', 100)
    self.assertRaises(AttributeError, setattr, x, 'imag', 100)
    self.assertRaises(AttributeError, setattr, x, 'conjugate', 100)
    self.assertRaises(AttributeError, setattr, x, '__complex__', 100)
