# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMedianGrouped_test_even_number_repeated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [5, 10, 10, 15, 20, 20, 20, 25, 25, 30]
    assert len(data) % 2 == 0
    self.assertApproxEqual(self.func(data, 5), 19.16666667, tol=1e-08)
    data = [2, 3, 4, 4, 4, 5]
    assert len(data) % 2 == 0
    self.assertApproxEqual(self.func(data), 3.83333333, tol=1e-08)
    data = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6]
    assert len(data) % 2 == 0
    self.assertEqual(self.func(data), 4.5)
    data = [3, 4, 4, 4, 5, 5, 5, 5, 6, 6]
    assert len(data) % 2 == 0
    self.assertEqual(self.func(data), 4.75)
