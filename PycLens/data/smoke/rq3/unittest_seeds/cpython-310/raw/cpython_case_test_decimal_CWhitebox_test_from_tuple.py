# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_from_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    localcontext = C.localcontext
    InvalidOperation = C.InvalidOperation
    Overflow = C.Overflow
    Underflow = C.Underflow
    with localcontext() as c:
        c.traps[InvalidOperation] = True
        c.traps[Overflow] = True
        c.traps[Underflow] = True
        x = (1, (), sys.maxsize)
        self.assertEqual(str(c.create_decimal(x)), '-0E+999999')
        self.assertRaises(InvalidOperation, Decimal, x)
        x = (1, (0, 1, 2), sys.maxsize)
        self.assertRaises(Overflow, c.create_decimal, x)
        self.assertRaises(InvalidOperation, Decimal, x)
        x = (1, (), -sys.maxsize - 1)
        self.assertEqual(str(c.create_decimal(x)), '-0E-1000007')
        self.assertRaises(InvalidOperation, Decimal, x)
        x = (1, (0, 1, 2), -sys.maxsize - 1)
        self.assertRaises(Underflow, c.create_decimal, x)
        self.assertRaises(InvalidOperation, Decimal, x)
        x = (1, (), sys.maxsize + 1)
        self.assertRaises(OverflowError, c.create_decimal, x)
        self.assertRaises(OverflowError, Decimal, x)
        x = (1, (), -sys.maxsize - 2)
        self.assertRaises(OverflowError, c.create_decimal, x)
        self.assertRaises(OverflowError, Decimal, x)
        x = (1, (), 'N')
        self.assertEqual(str(Decimal(x)), '-sNaN')
        x = (1, (0,), 'N')
        self.assertEqual(str(Decimal(x)), '-sNaN')
        x = (1, (0, 1), 'N')
        self.assertEqual(str(Decimal(x)), '-sNaN1')
