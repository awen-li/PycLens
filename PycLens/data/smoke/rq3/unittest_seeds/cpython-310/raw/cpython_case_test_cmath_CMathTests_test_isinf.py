# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_isinf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(cmath.isinf(1))
    self.assertFalse(cmath.isinf(1j))
    self.assertFalse(cmath.isinf(NAN))
    self.assertTrue(cmath.isinf(INF))
    self.assertTrue(cmath.isinf(complex(INF, 0)))
    self.assertTrue(cmath.isinf(complex(0, INF)))
    self.assertTrue(cmath.isinf(complex(INF, INF)))
    self.assertTrue(cmath.isinf(complex(NAN, INF)))
    self.assertTrue(cmath.isinf(complex(INF, NAN)))
