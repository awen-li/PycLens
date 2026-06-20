# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_isnan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(cmath.isnan(1))
    self.assertFalse(cmath.isnan(1j))
    self.assertFalse(cmath.isnan(INF))
    self.assertTrue(cmath.isnan(NAN))
    self.assertTrue(cmath.isnan(complex(NAN, 0)))
    self.assertTrue(cmath.isnan(complex(0, NAN)))
    self.assertTrue(cmath.isnan(complex(NAN, NAN)))
    self.assertTrue(cmath.isnan(complex(NAN, INF)))
    self.assertTrue(cmath.isnan(complex(INF, NAN)))
