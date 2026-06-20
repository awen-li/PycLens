# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_abs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for z in complex_zeros:
        self.assertEqual(abs(z), 0.0)
    for z in complex_infinities:
        self.assertEqual(abs(z), INF)
    self.assertEqual(abs(complex(NAN, -INF)), INF)
    self.assertTrue(math.isnan(abs(complex(NAN, -2.3))))
    self.assertTrue(math.isnan(abs(complex(NAN, -0.0))))
    self.assertTrue(math.isnan(abs(complex(NAN, 0.0))))
    self.assertTrue(math.isnan(abs(complex(NAN, 2.3))))
    self.assertEqual(abs(complex(NAN, INF)), INF)
    self.assertEqual(abs(complex(-INF, NAN)), INF)
    self.assertTrue(math.isnan(abs(complex(-2.3, NAN))))
    self.assertTrue(math.isnan(abs(complex(-0.0, NAN))))
    self.assertTrue(math.isnan(abs(complex(0.0, NAN))))
    self.assertTrue(math.isnan(abs(complex(2.3, NAN))))
    self.assertEqual(abs(complex(INF, NAN)), INF)
    self.assertTrue(math.isnan(abs(complex(NAN, NAN))))
