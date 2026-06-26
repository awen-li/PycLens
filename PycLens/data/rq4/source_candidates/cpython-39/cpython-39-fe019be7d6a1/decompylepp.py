# Source Generated with Decompyle++
# File: cpython-39-fe019be7d6a1.pyc (Python 3.9)


def __pybcsec_seed__():
    if object():
        if object():
            with object() as __pybcsec_self__:
                simple_real = (lambda .0: [ float(i) for i in .0 ])(range(-5, 6))
                simple_complex = (lambda .0: [ complex(x, y) for x in .0 for y in simple_real ])(simple_real)
                for x in simple_complex:
                    for y in simple_complex:
                        self.check_div(x, y)
                self.check_div(complex(1e+200, 1e+200), (1+0j))
                self.check_div(complex(1e-200, 1e-200), (1+0j))
                for i in range(100):
                    self.check_div(complex(random(), random()), complex(random(), random()))
                self.assertRaises(ZeroDivisionError, complex.__truediv__, (1+1j), (0+0j))
                self.assertRaises(OverflowError, pow, (1e+200+1j), (1e+200+1j))
                self.assertAlmostEqual(complex.__truediv__((2+0j), (1+1j)), (1+-1j))
                self.assertRaises(ZeroDivisionError, complex.__truediv__, (1+1j), (0+0j))
                for denom_real, denom_imag in ((0, NAN), (NAN, 0), (NAN, NAN)):
                    z = complex(0, 0) / complex(denom_real, denom_imag)
                    self.assertTrue(isnan(z.real))
                    self.assertTrue(isnan(z.imag))
                return None

if __name__ == '__main__':
    __pybcsec_seed__()
