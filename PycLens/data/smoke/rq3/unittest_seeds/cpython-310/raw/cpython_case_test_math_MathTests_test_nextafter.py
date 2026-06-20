# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: MathTests_test_nextafter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(math.nextafter(4503599627370496.0, -INF), 4503599627370495.5)
    self.assertEqual(math.nextafter(4503599627370496.0, INF), 4503599627370497.0)
    self.assertEqual(math.nextafter(9.223372036854776e+18, 0.0), 9.223372036854775e+18)
    self.assertEqual(math.nextafter(-9.223372036854776e+18, 0.0), -9.223372036854775e+18)
    self.assertEqual(math.nextafter(1.0, -INF), float.fromhex('0x1.fffffffffffffp-1'))
    self.assertEqual(math.nextafter(1.0, INF), float.fromhex('0x1.0000000000001p+0'))
    self.assertEqual(math.nextafter(2.0, 2.0), 2.0)
    self.assertEqualSign(math.nextafter(-0.0, +0.0), +0.0)
    self.assertEqualSign(math.nextafter(+0.0, -0.0), -0.0)
    smallest_subnormal = sys.float_info.min * sys.float_info.epsilon
    self.assertEqual(math.nextafter(+0.0, INF), smallest_subnormal)
    self.assertEqual(math.nextafter(-0.0, INF), smallest_subnormal)
    self.assertEqual(math.nextafter(+0.0, -INF), -smallest_subnormal)
    self.assertEqual(math.nextafter(-0.0, -INF), -smallest_subnormal)
    self.assertEqualSign(math.nextafter(smallest_subnormal, +0.0), +0.0)
    self.assertEqualSign(math.nextafter(-smallest_subnormal, +0.0), -0.0)
    self.assertEqualSign(math.nextafter(smallest_subnormal, -0.0), +0.0)
    self.assertEqualSign(math.nextafter(-smallest_subnormal, -0.0), -0.0)
    largest_normal = sys.float_info.max
    self.assertEqual(math.nextafter(INF, 0.0), largest_normal)
    self.assertEqual(math.nextafter(-INF, 0.0), -largest_normal)
    self.assertEqual(math.nextafter(largest_normal, INF), INF)
    self.assertEqual(math.nextafter(-largest_normal, -INF), -INF)
    self.assertIsNaN(math.nextafter(NAN, 1.0))
    self.assertIsNaN(math.nextafter(1.0, NAN))
    self.assertIsNaN(math.nextafter(NAN, NAN))
