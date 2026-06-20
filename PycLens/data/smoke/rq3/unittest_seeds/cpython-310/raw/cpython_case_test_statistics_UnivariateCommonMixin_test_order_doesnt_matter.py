# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: UnivariateCommonMixin_test_order_doesnt_matter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [1, 2, 3, 3, 3, 4, 5, 6] * 100
    expected = self.func(data)
    random.shuffle(data)
    actual = self.func(data)
    self.assertEqual(expected, actual)
