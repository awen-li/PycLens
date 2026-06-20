# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextFlags_test_float_operation_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    Inexact = self.decimal.Inexact
    FloatOperation = self.decimal.FloatOperation
    context = Context()
    self.assertFalse(context.flags[FloatOperation])
    self.assertFalse(context.traps[FloatOperation])
    context.clear_traps()
    context.traps[Inexact] = True
    context.traps[FloatOperation] = True
    self.assertTrue(context.traps[FloatOperation])
    self.assertTrue(context.traps[Inexact])
