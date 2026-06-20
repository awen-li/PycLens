# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: SpecialContexts_test_default_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DefaultContext = self.decimal.DefaultContext
    BasicContext = self.decimal.BasicContext
    ExtendedContext = self.decimal.ExtendedContext
    getcontext = self.decimal.getcontext
    setcontext = self.decimal.setcontext
    InvalidOperation = self.decimal.InvalidOperation
    DivisionByZero = self.decimal.DivisionByZero
    Overflow = self.decimal.Overflow
    self.assertEqual(BasicContext.prec, 9)
    self.assertEqual(ExtendedContext.prec, 9)
    assert_signals(self, DefaultContext, 'traps', [InvalidOperation, DivisionByZero, Overflow])
    savecontext = getcontext().copy()
    default_context_prec = DefaultContext.prec
    ex = None
    try:
        c = getcontext()
        saveprec = c.prec
        DefaultContext.prec = 961
        c = getcontext()
        self.assertEqual(c.prec, saveprec)
        setcontext(DefaultContext)
        c = getcontext()
        self.assertIsNot(c, DefaultContext)
        self.assertEqual(c.prec, 961)
    except Exception as e:
        ex = e.__class__
    finally:
        DefaultContext.prec = default_context_prec
        setcontext(savecontext)
        if ex:
            raise ex
