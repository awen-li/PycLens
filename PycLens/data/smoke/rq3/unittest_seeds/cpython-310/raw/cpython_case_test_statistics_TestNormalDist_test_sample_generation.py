# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_sample_generation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    (mu, sigma) = (10000, 3.0)
    X = NormalDist(mu, sigma)
    n = 1000
    data = X.samples(n)
    self.assertEqual(len(data), n)
    self.assertEqual(set(map(type, data)), {float})
    xbar = self.module.mean(data)
    self.assertTrue(mu - sigma * 8 <= xbar <= mu + sigma * 8)
    n = 100
    data1 = X.samples(n, seed='happiness and joy')
    data2 = X.samples(n, seed='trouble and despair')
    data3 = X.samples(n, seed='happiness and joy')
    data4 = X.samples(n, seed='trouble and despair')
    self.assertEqual(data1, data3)
    self.assertEqual(data2, data4)
    self.assertNotEqual(data1, data2)
