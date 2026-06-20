# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: RoundTestCase_test_small_n

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in [-308, -309, -400, 1 - 2 ** 31, -2 ** 31, -2 ** 31 - 1, -2 ** 100]:
        self.assertEqual(round(123.456, n), 0.0)
        self.assertEqual(round(-123.456, n), -0.0)
        self.assertEqual(round(1e+300, n), 0.0)
        self.assertEqual(round(1e-320, n), 0.0)
