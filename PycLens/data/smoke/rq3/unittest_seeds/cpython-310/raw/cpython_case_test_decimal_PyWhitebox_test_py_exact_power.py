# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PyWhitebox_test_py_exact_power

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = P.Decimal
    localcontext = P.localcontext
    with localcontext() as c:
        c.prec = 8
        x = Decimal(2 ** 16) ** Decimal('-0.5')
        self.assertEqual(x, Decimal('0.00390625'))
        x = Decimal(2 ** 16) ** Decimal('-0.6')
        self.assertEqual(x, Decimal('0.0012885819'))
        x = Decimal('256e7') ** Decimal('-0.5')
        x = Decimal(152587890625) ** Decimal('-0.0625')
        self.assertEqual(x, Decimal('0.2'))
        x = Decimal('152587890625e7') ** Decimal('-0.0625')
        x = Decimal(5 ** 2659) ** Decimal('-0.0625')
        c.prec = 1
        x = Decimal('152587890625') ** Decimal('-0.5')
        c.prec = 201
        x = Decimal(2 ** 578) ** Decimal('-0.5')
