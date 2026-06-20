# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_gauss

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for seed in (1, 12, 123, 1234, 12345, 123456, 654321):
        self.gen.seed(seed)
        x1 = self.gen.random()
        y1 = self.gen.gauss(0, 1)
        self.gen.seed(seed)
        x2 = self.gen.random()
        y2 = self.gen.gauss(0, 1)
        self.assertEqual(x1, x2)
        self.assertEqual(y1, y2)
