# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_same_type_addition_and_subtraction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    X = NormalDist(100, 12)
    Y = NormalDist(40, 5)
    self.assertEqual(X + Y, NormalDist(140, 13))
    self.assertEqual(X - Y, NormalDist(60, 13))
