# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: RoundTestCase_test_matches_float_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(500):
        x = i / 1000.0
        self.assertEqual(float(format(x, '.0f')), round(x, 0))
        self.assertEqual(float(format(x, '.1f')), round(x, 1))
        self.assertEqual(float(format(x, '.2f')), round(x, 2))
        self.assertEqual(float(format(x, '.3f')), round(x, 3))
    for i in range(5, 5000, 10):
        x = i / 1000.0
        self.assertEqual(float(format(x, '.0f')), round(x, 0))
        self.assertEqual(float(format(x, '.1f')), round(x, 1))
        self.assertEqual(float(format(x, '.2f')), round(x, 2))
        self.assertEqual(float(format(x, '.3f')), round(x, 3))
    for i in range(500):
        x = random.random()
        self.assertEqual(float(format(x, '.0f')), round(x, 0))
        self.assertEqual(float(format(x, '.1f')), round(x, 1))
        self.assertEqual(float(format(x, '.2f')), round(x, 2))
        self.assertEqual(float(format(x, '.3f')), round(x, 3))
