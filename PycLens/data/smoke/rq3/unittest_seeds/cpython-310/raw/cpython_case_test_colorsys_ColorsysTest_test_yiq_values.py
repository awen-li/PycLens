# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_colorsys.py
# case: ColorsysTest_test_yiq_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    values = [((0.0, 0.0, 0.0), (0.0, 0.0, 0.0)), ((0.0, 0.0, 1.0), (0.11, -0.3217, 0.3121)), ((0.0, 1.0, 0.0), (0.59, -0.2773, -0.5251)), ((0.0, 1.0, 1.0), (0.7, -0.599, -0.213)), ((1.0, 0.0, 0.0), (0.3, 0.599, 0.213)), ((1.0, 0.0, 1.0), (0.41, 0.2773, 0.5251)), ((1.0, 1.0, 0.0), (0.89, 0.3217, -0.3121)), ((1.0, 1.0, 1.0), (1.0, 0.0, 0.0)), ((0.5, 0.5, 0.5), (0.5, 0.0, 0.0))]
    for (rgb, yiq) in values:
        self.assertTripleEqual(yiq, colorsys.rgb_to_yiq(*rgb))
        self.assertTripleEqual(rgb, colorsys.yiq_to_rgb(*yiq))
