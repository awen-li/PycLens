# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_numeric_tower.py
# case: HashTest_test_binary_floats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_equal_hash(0.0, -0.0)
    self.check_equal_hash(0.0, D(0))
    self.check_equal_hash(-0.0, D(0))
    self.check_equal_hash(-0.0, D('-0.0'))
    self.check_equal_hash(0.0, F(0))
    self.check_equal_hash(float('inf'), D('inf'))
    self.check_equal_hash(float('-inf'), D('-inf'))
    for _ in range(1000):
        x = random.random() * math.exp(random.random() * 200.0 - 100.0)
        self.check_equal_hash(x, D.from_float(x))
        self.check_equal_hash(x, F.from_float(x))
