# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_richcompare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(complex.__eq__(1 + 1j, 1 << 10000), False)
    self.assertIs(complex.__lt__(1 + 1j, None), NotImplemented)
    self.assertIs(complex.__eq__(1 + 1j, 1 + 1j), True)
    self.assertIs(complex.__eq__(1 + 1j, 2 + 2j), False)
    self.assertIs(complex.__ne__(1 + 1j, 1 + 1j), False)
    self.assertIs(complex.__ne__(1 + 1j, 2 + 2j), True)
    for i in range(1, 100):
        f = i / 100.0
        self.assertIs(complex.__eq__(f + 0j, f), True)
        self.assertIs(complex.__ne__(f + 0j, f), False)
        self.assertIs(complex.__eq__(complex(f, f), f), False)
        self.assertIs(complex.__ne__(complex(f, f), f), True)
    self.assertIs(complex.__lt__(1 + 1j, 2 + 2j), NotImplemented)
    self.assertIs(complex.__le__(1 + 1j, 2 + 2j), NotImplemented)
    self.assertIs(complex.__gt__(1 + 1j, 2 + 2j), NotImplemented)
    self.assertIs(complex.__ge__(1 + 1j, 2 + 2j), NotImplemented)
    self.assertRaises(TypeError, operator.lt, 1 + 1j, 2 + 2j)
    self.assertRaises(TypeError, operator.le, 1 + 1j, 2 + 2j)
    self.assertRaises(TypeError, operator.gt, 1 + 1j, 2 + 2j)
    self.assertRaises(TypeError, operator.ge, 1 + 1j, 2 + 2j)
    self.assertIs(operator.eq(1 + 1j, 1 + 1j), True)
    self.assertIs(operator.eq(1 + 1j, 2 + 2j), False)
    self.assertIs(operator.ne(1 + 1j, 1 + 1j), False)
    self.assertIs(operator.ne(1 + 1j, 2 + 2j), True)
