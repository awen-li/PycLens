# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMean_test_mismatched_infs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [2, 4, 6, float('inf'), 1, 3, 5, float('-inf')]
    result = self.func(data)
    self.assertTrue(math.isnan(result))
