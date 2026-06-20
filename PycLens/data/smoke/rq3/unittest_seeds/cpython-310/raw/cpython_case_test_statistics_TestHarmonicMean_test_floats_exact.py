# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestHarmonicMean_test_floats_exact

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [1 / 8, 1 / 4, 1 / 4, 1 / 2, 1 / 2]
    random.shuffle(data)
    self.assertEqual(self.func(data), 1 / 4)
    self.assertEqual(self.func([0.25, 0.5, 1.0, 1.0]), 0.5)
