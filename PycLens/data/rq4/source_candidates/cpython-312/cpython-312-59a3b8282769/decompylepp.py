# Source Generated with Decompyle++
# File: cpython-312-59a3b8282769.pyc (Python 3.12)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = Decimal
    import decimal
    decimal_examples = [
        (Decimal('1.00000001'), Decimal('1.0')),
        (Decimal('1.00000001e-20'), Decimal('1.0e-20')),
        (Decimal('1.00000001e-100'), None('1.0e-100')),
        (Decimal('1.00000001e20'), Decimal('1.0e20'))]
    self.assertAllClose(decimal_examples, rel_tol = 1e-08)
    self.assertAllNotClose(decimal_examples, rel_tol = 1e-09)

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
