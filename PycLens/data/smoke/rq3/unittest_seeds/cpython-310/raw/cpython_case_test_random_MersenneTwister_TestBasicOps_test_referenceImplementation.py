# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_referenceImplementation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = [0.4583980307371326, 0.8605781520197878, 0.9284833172678215, 0.3593268111978246, 0.08182349376244957, 0.1433222647016933, 0.08429782382352002, 0.5381486467183145, 0.0892150249119934, 0.7848619610537291]
    self.gen.seed(61731 + (24903 << 32) + (614 << 64) + (42143 << 96))
    actual = self.randomlist(2000)[-10:]
    for (a, e) in zip(actual, expected):
        self.assertAlmostEqual(a, e, places=14)
