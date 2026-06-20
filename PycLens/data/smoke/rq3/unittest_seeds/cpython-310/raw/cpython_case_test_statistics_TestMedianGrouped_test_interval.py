# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMedianGrouped_test_interval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [2.25, 2.5, 2.5, 2.75, 2.75, 3.0, 3.0, 3.25, 3.5, 3.75]
    self.assertEqual(self.func(data, 0.25), 2.875)
    data = [2.25, 2.5, 2.5, 2.75, 2.75, 2.75, 3.0, 3.0, 3.25, 3.5, 3.75]
    self.assertApproxEqual(self.func(data, 0.25), 2.83333333, tol=1e-08)
    data = [220, 220, 240, 260, 260, 260, 260, 280, 280, 300, 320, 340]
    self.assertEqual(self.func(data, 20), 265.0)
