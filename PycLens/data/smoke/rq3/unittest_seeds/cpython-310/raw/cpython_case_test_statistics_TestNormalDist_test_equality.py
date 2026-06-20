# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    nd1 = NormalDist()
    nd2 = NormalDist(2, 4)
    nd3 = NormalDist()
    nd4 = NormalDist(2, 4)
    nd5 = NormalDist(2, 8)
    nd6 = NormalDist(8, 4)
    self.assertNotEqual(nd1, nd2)
    self.assertEqual(nd1, nd3)
    self.assertEqual(nd2, nd4)
    self.assertNotEqual(nd2, nd5)
    self.assertNotEqual(nd2, nd6)

    class A:

        def __eq__(self, other):
            return 10
    a = A()
    self.assertEqual(nd1.__eq__(a), NotImplemented)
    self.assertEqual(nd1 == a, 10)
    self.assertEqual(a == nd1, 10)

    class SizedNormalDist(NormalDist):

        def __init__(self, mu, sigma, n):
            super().__init__(mu, sigma)
            self.n = n
    s = SizedNormalDist(100, 15, 57)
    nd4 = NormalDist(100, 15)
    self.assertEqual(s, nd4)

    class LognormalDist:

        def __init__(self, mu, sigma):
            self.mu = mu
            self.sigma = sigma
    lnd = LognormalDist(100, 15)
    nd = NormalDist(100, 15)
    self.assertNotEqual(nd, lnd)
