# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_hash_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    localcontext = self.decimal.localcontext

    def hashit(d):
        a = hash(d)
        b = d.__hash__()
        self.assertEqual(a, b)
        return a
    hashit(Decimal(23))
    hashit(Decimal('Infinity'))
    hashit(Decimal('-Infinity'))
    hashit(Decimal('nan123'))
    hashit(Decimal('-NaN'))
    test_values = [Decimal(sign * (2 ** m + n)) for m in [0, 14, 15, 16, 17, 30, 31, 32, 33, 61, 62, 63, 64, 65, 66] for n in range(-10, 10) for sign in [-1, 1]]
    test_values.extend([Decimal('-1'), Decimal('-0'), Decimal('0.00'), Decimal('-0.000'), Decimal('0E10'), Decimal('-0E12'), Decimal('10.0'), Decimal('-23.00000'), Decimal('1230E100'), Decimal('-4.5678E50'), Decimal(2 ** 64 + 2 ** 32 - 1), Decimal('1.634E100'), Decimal('90.697E100'), Decimal('188.83E100'), Decimal('1652.9E100'), Decimal('56531E100')])
    for value in test_values:
        self.assertEqual(hashit(value), hash(int(value)))
    test_strings = ['inf', '-Inf', '0.0', '-.0e1', '34.0', '2.5', '112390.625', '-0.515625']
    for s in test_strings:
        f = float(s)
        d = Decimal(s)
        self.assertEqual(hashit(d), hash(f))
    with localcontext() as c:
        x = Decimal('123456789.1')
        c.prec = 6
        h1 = hashit(x)
        c.prec = 10
        h2 = hashit(x)
        c.prec = 16
        h3 = hashit(x)
        self.assertEqual(h1, h2)
        self.assertEqual(h1, h3)
        c.prec = 10000
        x = 1100 ** 1248
        self.assertEqual(hashit(Decimal(x)), hashit(x))
