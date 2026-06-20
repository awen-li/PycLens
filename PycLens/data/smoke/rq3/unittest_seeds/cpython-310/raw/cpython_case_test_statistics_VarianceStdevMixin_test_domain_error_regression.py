# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: VarianceStdevMixin_test_domain_error_regression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [0.123456789012345] * 10000
    result = self.func(data)
    self.assertApproxEqual(result, 0.0, tol=5e-17)
    self.assertGreaterEqual(result, 0)
