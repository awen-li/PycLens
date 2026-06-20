# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_alternative_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    data = [96, 107, 90, 92, 110]
    self.assertEqual(NormalDist.from_samples(data), NormalDist(99, 9))
    self.assertEqual(NormalDist.from_samples(tuple(data)), NormalDist(99, 9))
    self.assertEqual(NormalDist.from_samples(iter(data)), NormalDist(99, 9))
    with self.assertRaises(self.module.StatisticsError):
        NormalDist.from_samples([])
    with self.assertRaises(self.module.StatisticsError):
        NormalDist.from_samples([10])

    class NewNormalDist(NormalDist):
        pass
    nnd = NewNormalDist.from_samples(data)
    self.assertEqual(type(nnd), NewNormalDist)
