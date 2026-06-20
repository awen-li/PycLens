# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: RoundTestCase_test_large_n

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in [324, 325, 400, 2 ** 31 - 1, 2 ** 31, 2 ** 32, 2 ** 100]:
        self.assertEqual(round(123.456, n), 123.456)
        self.assertEqual(round(-123.456, n), -123.456)
        self.assertEqual(round(1e+300, n), 1e+300)
        self.assertEqual(round(1e-320, n), 1e-320)
    self.assertEqual(round(1e+150, 300), 1e+150)
    self.assertEqual(round(1e+300, 307), 1e+300)
    self.assertEqual(round(-3.1415, 308), -3.1415)
    self.assertEqual(round(1e+150, 309), 1e+150)
    self.assertEqual(round(1.4e-315, 315), 1e-315)
