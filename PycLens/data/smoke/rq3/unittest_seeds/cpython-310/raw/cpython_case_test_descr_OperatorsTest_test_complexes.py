# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: OperatorsTest_test_complexes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.number_operators(100j, 3j, skip=['lt', 'le', 'gt', 'ge', 'int', 'float', 'floordiv', 'divmod', 'mod'])

    class Number(complex):
        __slots__ = ['prec']

        def __new__(cls, *args, **kwds):
            result = complex.__new__(cls, *args)
            result.prec = kwds.get('prec', 12)
            return result

        def __repr__(self):
            prec = self.prec
            if self.imag == 0.0:
                return '%.*g' % (prec, self.real)
            if self.real == 0.0:
                return '%.*gj' % (prec, self.imag)
            return '(%.*g+%.*gj)' % (prec, self.real, prec, self.imag)
        __str__ = __repr__
    a = Number(3.14, prec=6)
    self.assertEqual(repr(a), '3.14')
    self.assertEqual(a.prec, 6)
    a = Number(a, prec=2)
    self.assertEqual(repr(a), '3.1')
    self.assertEqual(a.prec, 2)
    a = Number(234.5)
    self.assertEqual(repr(a), '234.5')
    self.assertEqual(a.prec, 12)
