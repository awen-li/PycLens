# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(complex('1e500'), complex(INF, 0.0))
    self.assertEqual(complex('-1e500j'), complex(0.0, -INF))
    self.assertEqual(complex('-1e500+1.8e308j'), complex(-INF, INF))
