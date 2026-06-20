# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_choices_infinite_total

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        self.gen.choices('A', [float('inf')])
    with self.assertRaises(ValueError):
        self.gen.choices('AB', [0.0, float('inf')])
    with self.assertRaises(ValueError):
        self.gen.choices('AB', [-float('inf'), 123])
    with self.assertRaises(ValueError):
        self.gen.choices('AB', [0.0, float('nan')])
    with self.assertRaises(ValueError):
        self.gen.choices('AB', [float('-inf'), float('inf')])
