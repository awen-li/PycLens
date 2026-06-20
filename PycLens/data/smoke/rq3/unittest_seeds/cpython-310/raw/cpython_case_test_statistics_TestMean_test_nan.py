# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMean_test_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = [1, 3, 5, 7, 9]
    for kind in (float, Decimal):
        inf = kind('nan')
        data = raw + [inf]
        result = self.func(data)
        self.assertTrue(math.isnan(result))
