# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestHarmonicMean_test_ints

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [2, 4, 4, 8, 16, 16]
    random.shuffle(data)
    self.assertEqual(self.func(data), 6 * 4 / 5)
