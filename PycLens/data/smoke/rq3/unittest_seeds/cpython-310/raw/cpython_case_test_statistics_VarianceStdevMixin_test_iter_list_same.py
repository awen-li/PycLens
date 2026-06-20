# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: VarianceStdevMixin_test_iter_list_same

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [random.uniform(-3, 8) for _ in range(1000)]
    expected = self.func(data)
    self.assertEqual(self.func(iter(data)), expected)
