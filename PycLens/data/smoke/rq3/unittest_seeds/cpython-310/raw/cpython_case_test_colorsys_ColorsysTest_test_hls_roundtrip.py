# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_colorsys.py
# case: ColorsysTest_test_hls_roundtrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for r in frange(0.0, 1.0, 0.2):
        for g in frange(0.0, 1.0, 0.2):
            for b in frange(0.0, 1.0, 0.2):
                rgb = (r, g, b)
                self.assertTripleEqual(rgb, colorsys.hls_to_rgb(*colorsys.rgb_to_hls(*rgb)))
