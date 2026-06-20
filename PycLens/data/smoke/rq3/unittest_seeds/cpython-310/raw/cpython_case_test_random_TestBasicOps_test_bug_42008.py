# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_bug_42008

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _random
    r1 = _random.Random()
    r1.seed(8675309)
    r2 = _random.Random(8675309)
    self.assertEqual(r1.random(), r2.random())
