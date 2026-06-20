# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ArithmeticOperatorsTest_test_nan_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    InvalidOperation = self.decimal.InvalidOperation
    localcontext = self.decimal.localcontext
    n = Decimal('NaN')
    s = Decimal('sNaN')
    i = Decimal('Inf')
    f = Decimal('2')
    qnan_pairs = ((n, n), (n, i), (i, n), (n, f), (f, n))
    snan_pairs = ((s, n), (n, s), (s, i), (i, s), (s, f), (f, s), (s, s))
    order_ops = (operator.lt, operator.le, operator.gt, operator.ge)
    equality_ops = (operator.eq, operator.ne)
    for (x, y) in qnan_pairs + snan_pairs:
        for op in order_ops + equality_ops:
            got = op(x, y)
            expected = True if op is operator.ne else False
            self.assertIs(expected, got, 'expected {0!r} for operator.{1}({2!r}, {3!r}); got {4!r}'.format(expected, op.__name__, x, y, got))
    with localcontext() as ctx:
        ctx.traps[InvalidOperation] = 1
        for (x, y) in qnan_pairs:
            for op in equality_ops:
                got = op(x, y)
                expected = True if op is operator.ne else False
                self.assertIs(expected, got, 'expected {0!r} for operator.{1}({2!r}, {3!r}); got {4!r}'.format(expected, op.__name__, x, y, got))
        for (x, y) in snan_pairs:
            for op in equality_ops:
                self.assertRaises(InvalidOperation, operator.eq, x, y)
                self.assertRaises(InvalidOperation, operator.ne, x, y)
        for (x, y) in qnan_pairs + snan_pairs:
            for op in order_ops:
                self.assertRaises(InvalidOperation, op, x, y)
