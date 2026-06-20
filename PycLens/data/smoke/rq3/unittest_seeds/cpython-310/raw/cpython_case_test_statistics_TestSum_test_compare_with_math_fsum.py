# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestSum_test_compare_with_math_fsum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [random.uniform(-100, 1000) for _ in range(1000)]
    self.assertApproxEqual(float(self.func(data)[1]), math.fsum(data), rel=2e-16)
