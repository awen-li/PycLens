# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_hashability

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ND = self.module.NormalDist
    s = {ND(100, 15), ND(100.0, 15.0), ND(100, 10), ND(95, 15), ND(100, 15)}
    self.assertEqual(len(s), 3)
