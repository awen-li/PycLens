# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ImplicitConstructionTest_test_rop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal

    class E:

        def __divmod__(self, other):
            return 'divmod ' + str(other)

        def __rdivmod__(self, other):
            return str(other) + ' rdivmod'

        def __lt__(self, other):
            return 'lt ' + str(other)

        def __gt__(self, other):
            return 'gt ' + str(other)

        def __le__(self, other):
            return 'le ' + str(other)

        def __ge__(self, other):
            return 'ge ' + str(other)

        def __eq__(self, other):
            return 'eq ' + str(other)

        def __ne__(self, other):
            return 'ne ' + str(other)
    self.assertEqual(divmod(E(), Decimal(10)), 'divmod 10')
    self.assertEqual(divmod(Decimal(10), E()), '10 rdivmod')
    self.assertEqual(eval('Decimal(10) < E()'), 'gt 10')
    self.assertEqual(eval('Decimal(10) > E()'), 'lt 10')
    self.assertEqual(eval('Decimal(10) <= E()'), 'ge 10')
    self.assertEqual(eval('Decimal(10) >= E()'), 'le 10')
    self.assertEqual(eval('Decimal(10) == E()'), 'eq 10')
    self.assertEqual(eval('Decimal(10) != E()'), 'ne 10')
    oplist = [('+', '__add__', '__radd__'), ('-', '__sub__', '__rsub__'), ('*', '__mul__', '__rmul__'), ('/', '__truediv__', '__rtruediv__'), ('%', '__mod__', '__rmod__'), ('//', '__floordiv__', '__rfloordiv__'), ('**', '__pow__', '__rpow__')]
    for (sym, lop, rop) in oplist:
        setattr(E, lop, lambda self, other: 'str' + lop + str(other))
        setattr(E, rop, lambda self, other: str(other) + rop + 'str')
        self.assertEqual(eval('E()' + sym + 'Decimal(10)'), 'str' + lop + '10')
        self.assertEqual(eval('Decimal(10)' + sym + 'E()'), '10' + rop + 'str')
