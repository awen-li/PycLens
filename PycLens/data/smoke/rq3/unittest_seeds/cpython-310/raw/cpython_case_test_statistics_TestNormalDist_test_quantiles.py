# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_quantiles

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Z = self.module.NormalDist()
    for (n, expected) in [(1, []), (2, [0.0]), (3, [-0.4307, 0.4307]), (4, [-0.6745, 0.0, 0.6745])]:
        actual = Z.quantiles(n=n)
        self.assertTrue(all((math.isclose(e, a, abs_tol=0.0001) for (e, a) in zip(expected, actual))))
