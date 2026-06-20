# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: SumSpecialValues_test_float_mismatched_infs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    inf = float('inf')
    result = statistics._sum([1, 2, inf, 3, -inf, 4])[1]
    self.assertTrue(math.isnan(result))
