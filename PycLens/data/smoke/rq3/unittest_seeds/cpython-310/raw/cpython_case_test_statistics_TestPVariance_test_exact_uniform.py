# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestPVariance_test_exact_uniform

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = list(range(10000))
    random.shuffle(data)
    expected = (10000 ** 2 - 1) / 12
    self.assertEqual(self.func(data), expected)
