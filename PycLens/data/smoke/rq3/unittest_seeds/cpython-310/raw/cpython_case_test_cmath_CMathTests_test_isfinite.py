# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_isfinite

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    real_vals = [float('-inf'), -2.3, -0.0, 0.0, 2.3, float('inf'), float('nan')]
    for x in real_vals:
        for y in real_vals:
            z = complex(x, y)
            self.assertEqual(cmath.isfinite(z), math.isfinite(x) and math.isfinite(y))
