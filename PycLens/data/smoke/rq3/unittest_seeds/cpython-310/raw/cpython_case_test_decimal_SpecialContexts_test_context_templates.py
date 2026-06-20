# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: SpecialContexts_test_context_templates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    BasicContext = self.decimal.BasicContext
    ExtendedContext = self.decimal.ExtendedContext
    getcontext = self.decimal.getcontext
    setcontext = self.decimal.setcontext
    InvalidOperation = self.decimal.InvalidOperation
    DivisionByZero = self.decimal.DivisionByZero
    Overflow = self.decimal.Overflow
    Underflow = self.decimal.Underflow
    Clamped = self.decimal.Clamped
    assert_signals(self, BasicContext, 'traps', [InvalidOperation, DivisionByZero, Overflow, Underflow, Clamped])
    savecontext = getcontext().copy()
    basic_context_prec = BasicContext.prec
    extended_context_prec = ExtendedContext.prec
    ex = None
    try:
        BasicContext.prec = ExtendedContext.prec = 441
        for template in (BasicContext, ExtendedContext):
            setcontext(template)
            c = getcontext()
            self.assertIsNot(c, template)
            self.assertEqual(c.prec, 441)
    except Exception as e:
        ex = e.__class__
    finally:
        BasicContext.prec = basic_context_prec
        ExtendedContext.prec = extended_context_prec
        setcontext(savecontext)
        if ex:
            raise ex
