# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: IsCloseTests_test_eight_decimal_places

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eight_decimal_places_examples = [(100000000.0, 100000000.0 + 1), (-1e-08, -1.000000009e-08), (1.12345678, 1.12345679)]
    self.assertAllClose(eight_decimal_places_examples, rel_tol=1e-08)
    self.assertAllNotClose(eight_decimal_places_examples, rel_tol=1e-09)
