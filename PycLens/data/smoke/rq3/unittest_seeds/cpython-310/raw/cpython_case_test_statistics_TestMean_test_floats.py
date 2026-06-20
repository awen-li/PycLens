# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMean_test_floats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [17.25, 19.75, 20.0, 21.5, 21.75, 23.25, 25.125, 27.5]
    random.shuffle(data)
    self.assertEqual(self.func(data), 22.015625)
