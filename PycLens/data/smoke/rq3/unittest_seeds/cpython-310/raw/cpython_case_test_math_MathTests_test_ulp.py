# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: MathTests_test_ulp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(math.ulp(1.0), sys.float_info.epsilon)
    self.assertEqual(math.ulp(2 ** 52), 1.0)
    self.assertEqual(math.ulp(2 ** 53), 2.0)
    self.assertEqual(math.ulp(2 ** 64), 4096.0)
    self.assertEqual(math.ulp(0.0), sys.float_info.min * sys.float_info.epsilon)
    self.assertEqual(math.ulp(FLOAT_MAX), FLOAT_MAX - math.nextafter(FLOAT_MAX, -INF))
    self.assertEqual(math.ulp(INF), INF)
    self.assertIsNaN(math.ulp(math.nan))
    for x in (0.0, 1.0, 2 ** 52, 2 ** 64, INF):
        with self.subTest(x=x):
            self.assertEqual(math.ulp(-x), math.ulp(x))
