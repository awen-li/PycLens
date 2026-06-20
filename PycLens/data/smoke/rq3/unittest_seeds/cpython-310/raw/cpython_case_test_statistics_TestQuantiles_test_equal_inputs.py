# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestQuantiles_test_equal_inputs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    quantiles = statistics.quantiles
    for n in range(2, 10):
        data = [10.0] * n
        self.assertEqual(quantiles(data), [10.0, 10.0, 10.0])
        self.assertEqual(quantiles(data, method='inclusive'), [10.0, 10.0, 10.0])
