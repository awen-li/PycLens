# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_instantiation_and_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd = self.module.NormalDist(500, 17)
    self.assertEqual(nd.mean, 500)
    self.assertEqual(nd.stdev, 17)
    self.assertEqual(nd.variance, 17 ** 2)
    nd = self.module.NormalDist()
    self.assertEqual(nd.mean, 0)
    self.assertEqual(nd.stdev, 1)
    self.assertEqual(nd.variance, 1 ** 2)
    with self.assertRaises(self.module.StatisticsError):
        self.module.NormalDist(500, -10)

    class NewNormalDist(self.module.NormalDist):
        pass
    nnd = NewNormalDist(200, 5)
    self.assertEqual(type(nnd), NewNormalDist)
