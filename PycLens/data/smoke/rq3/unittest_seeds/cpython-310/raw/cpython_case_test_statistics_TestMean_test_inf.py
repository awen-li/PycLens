# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMean_test_inf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = [1, 3, 5, 7, 9]
    for kind in (float, Decimal):
        for sign in (1, -1):
            inf = kind('inf') * sign
            data = raw + [inf]
            result = self.func(data)
            self.assertTrue(math.isinf(result))
            self.assertEqual(result, inf)
