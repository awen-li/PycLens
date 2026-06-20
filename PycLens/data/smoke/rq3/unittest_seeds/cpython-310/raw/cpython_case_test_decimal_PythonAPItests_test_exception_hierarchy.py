# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PythonAPItests_test_exception_hierarchy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decimal = self.decimal
    DecimalException = decimal.DecimalException
    InvalidOperation = decimal.InvalidOperation
    FloatOperation = decimal.FloatOperation
    DivisionByZero = decimal.DivisionByZero
    Overflow = decimal.Overflow
    Underflow = decimal.Underflow
    Subnormal = decimal.Subnormal
    Inexact = decimal.Inexact
    Rounded = decimal.Rounded
    Clamped = decimal.Clamped
    self.assertTrue(issubclass(DecimalException, ArithmeticError))
    self.assertTrue(issubclass(InvalidOperation, DecimalException))
    self.assertTrue(issubclass(FloatOperation, DecimalException))
    self.assertTrue(issubclass(FloatOperation, TypeError))
    self.assertTrue(issubclass(DivisionByZero, DecimalException))
    self.assertTrue(issubclass(DivisionByZero, ZeroDivisionError))
    self.assertTrue(issubclass(Overflow, Rounded))
    self.assertTrue(issubclass(Overflow, Inexact))
    self.assertTrue(issubclass(Overflow, DecimalException))
    self.assertTrue(issubclass(Underflow, Inexact))
    self.assertTrue(issubclass(Underflow, Rounded))
    self.assertTrue(issubclass(Underflow, Subnormal))
    self.assertTrue(issubclass(Underflow, DecimalException))
    self.assertTrue(issubclass(Subnormal, DecimalException))
    self.assertTrue(issubclass(Inexact, DecimalException))
    self.assertTrue(issubclass(Rounded, DecimalException))
    self.assertTrue(issubclass(Clamped, DecimalException))
    self.assertTrue(issubclass(decimal.ConversionSyntax, InvalidOperation))
    self.assertTrue(issubclass(decimal.DivisionImpossible, InvalidOperation))
    self.assertTrue(issubclass(decimal.DivisionUndefined, InvalidOperation))
    self.assertTrue(issubclass(decimal.DivisionUndefined, ZeroDivisionError))
    self.assertTrue(issubclass(decimal.InvalidContext, InvalidOperation))
