# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_pow_with_small_integer_exponents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    values = [complex(5.0, 12.0), complex(5e+100, 1.2e+101), complex(-4.0, INF), complex(INF, 0.0)]
    exponents = [-19, -5, -3, -2, -1, 0, 1, 2, 3, 5, 19]
    for value in values:
        for exponent in exponents:
            with self.subTest(value=value, exponent=exponent):
                try:
                    int_pow = value ** exponent
                except OverflowError:
                    int_pow = 'overflow'
                try:
                    float_pow = value ** float(exponent)
                except OverflowError:
                    float_pow = 'overflow'
                try:
                    complex_pow = value ** complex(exponent)
                except OverflowError:
                    complex_pow = 'overflow'
                self.assertEqual(str(float_pow), str(int_pow))
                self.assertEqual(str(complex_pow), str(int_pow))
