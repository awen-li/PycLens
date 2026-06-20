# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd = self.module.NormalDist(37.5, 5.625)
    nd1 = copy.copy(nd)
    self.assertEqual(nd, nd1)
    nd2 = copy.deepcopy(nd)
    self.assertEqual(nd, nd2)
