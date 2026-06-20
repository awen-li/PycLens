# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_cmath_matches_math

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_values = [0.01, 0.1, 0.2, 0.5, 0.9, 0.99]
    unit_interval = test_values + [-x for x in test_values] + [0.0, 1.0, -1.0]
    positive = test_values + [1.0] + [1.0 / x for x in test_values]
    nonnegative = [0.0] + positive
    real_line = [0.0] + positive + [-x for x in positive]
    test_functions = {'acos': unit_interval, 'asin': unit_interval, 'atan': real_line, 'cos': real_line, 'cosh': real_line, 'exp': real_line, 'log': positive, 'log10': positive, 'sin': real_line, 'sinh': real_line, 'sqrt': nonnegative, 'tan': real_line, 'tanh': real_line}
    for (fn, values) in test_functions.items():
        float_fn = getattr(math, fn)
        complex_fn = getattr(cmath, fn)
        for v in values:
            z = complex_fn(v)
            self.rAssertAlmostEqual(float_fn(v), z.real)
            self.assertEqual(0.0, z.imag)
    for base in [0.5, 2.0, 10.0]:
        for v in positive:
            z = cmath.log(v, base)
            self.rAssertAlmostEqual(math.log(v, base), z.real)
            self.assertEqual(0.0, z.imag)
