# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestSum_test_mixed_sum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.func, [1, 2.0, Decimal(1)])
    self.assertRaises(TypeError, self.func, [1, 2.0], Decimal(1))
