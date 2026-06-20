# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMedianGrouped_test_odd_number_repeated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [12, 13, 14, 14, 14, 15, 15]
    assert len(data) % 2 == 1
    self.assertEqual(self.func(data), 14)
    data = [12, 13, 14, 14, 14, 14, 15]
    assert len(data) % 2 == 1
    self.assertEqual(self.func(data), 13.875)
    data = [5, 10, 10, 15, 20, 20, 20, 20, 25, 25, 30]
    assert len(data) % 2 == 1
    self.assertEqual(self.func(data, 5), 19.375)
    data = [16, 18, 18, 18, 18, 20, 20, 20, 22, 22, 22, 24, 24, 26, 28]
    assert len(data) % 2 == 1
    self.assertApproxEqual(self.func(data, 2), 20.66666667, tol=1e-08)
