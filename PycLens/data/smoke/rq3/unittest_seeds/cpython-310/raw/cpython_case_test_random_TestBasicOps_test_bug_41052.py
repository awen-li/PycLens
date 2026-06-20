# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_bug_41052

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _random
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        r = _random.Random()
        self.assertRaises(TypeError, pickle.dumps, r, proto)
