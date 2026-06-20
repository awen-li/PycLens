# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ExactRatioTest_test_float_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NAN = float('NAN')

    class MyFloat(float):
        pass
    for nan in (NAN, MyFloat(NAN)):
        ratio = statistics._exact_ratio(nan)
        self.assertTrue(math.isnan(ratio[0]))
        self.assertIs(ratio[1], None)
        self.assertEqual(type(ratio[0]), type(nan))
