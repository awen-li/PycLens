# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strtod.py
# case: StrtodTests_test_large_exponents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def positive_exp(n):
        """ Long string with value 1.0 and exponent n"""
        return '0.{}1e+{}'.format('0' * (n - 1), n)

    def negative_exp(n):
        """ Long string with value 1.0 and exponent -n"""
        return '1{}e-{}'.format('0' * n, n)
    self.assertEqual(float(positive_exp(10000)), 1.0)
    self.assertEqual(float(positive_exp(20000)), 1.0)
    self.assertEqual(float(positive_exp(30000)), 1.0)
    self.assertEqual(float(negative_exp(10000)), 1.0)
    self.assertEqual(float(negative_exp(20000)), 1.0)
    self.assertEqual(float(negative_exp(30000)), 1.0)
