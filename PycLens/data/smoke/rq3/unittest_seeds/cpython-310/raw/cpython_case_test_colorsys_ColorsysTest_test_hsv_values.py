# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_colorsys.py
# case: ColorsysTest_test_hsv_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    values = [((0.0, 0.0, 0.0), (0, 0.0, 0.0)), ((0.0, 0.0, 1.0), (4.0 / 6.0, 1.0, 1.0)), ((0.0, 1.0, 0.0), (2.0 / 6.0, 1.0, 1.0)), ((0.0, 1.0, 1.0), (3.0 / 6.0, 1.0, 1.0)), ((1.0, 0.0, 0.0), (0, 1.0, 1.0)), ((1.0, 0.0, 1.0), (5.0 / 6.0, 1.0, 1.0)), ((1.0, 1.0, 0.0), (1.0 / 6.0, 1.0, 1.0)), ((1.0, 1.0, 1.0), (0, 0.0, 1.0)), ((0.5, 0.5, 0.5), (0, 0.0, 0.5))]
    for (rgb, hsv) in values:
        self.assertTripleEqual(hsv, colorsys.rgb_to_hsv(*rgb))
        self.assertTripleEqual(rgb, colorsys.hsv_to_rgb(*hsv))
