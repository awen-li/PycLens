# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_strong_reference_implementation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from math import ldexp
    expected = [4128882400830239, 7751398889519013, 8363034243334166, 3236528186029503, 737000512037440, 1290932195808883, 759287295919497, 4847212089661076, 803577505899006, 7069408070677702]
    self.gen.seed(61731 + (24903 << 32) + (614 << 64) + (42143 << 96))
    actual = self.randomlist(2000)[-10:]
    for (a, e) in zip(actual, expected):
        self.assertEqual(int(ldexp(a, 53)), e)
