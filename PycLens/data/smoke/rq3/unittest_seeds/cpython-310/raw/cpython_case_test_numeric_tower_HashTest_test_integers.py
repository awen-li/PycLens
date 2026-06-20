# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_numeric_tower.py
# case: HashTest_test_integers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(-1000, 1000):
        self.check_equal_hash(i, float(i))
        self.check_equal_hash(i, D(i))
        self.check_equal_hash(i, F(i))
    for i in range(100):
        n = 2 ** i - 1
        if n == int(float(n)):
            self.check_equal_hash(n, float(n))
            self.check_equal_hash(-n, -float(n))
        self.check_equal_hash(n, D(n))
        self.check_equal_hash(n, F(n))
        self.check_equal_hash(-n, D(-n))
        self.check_equal_hash(-n, F(-n))
        n = 2 ** i
        self.check_equal_hash(n, float(n))
        self.check_equal_hash(-n, -float(n))
        self.check_equal_hash(n, D(n))
        self.check_equal_hash(n, F(n))
        self.check_equal_hash(-n, D(-n))
        self.check_equal_hash(-n, F(-n))
    for _ in range(1000):
        e = random.randrange(300)
        n = random.randrange(-10 ** e, 10 ** e)
        self.check_equal_hash(n, D(n))
        self.check_equal_hash(n, F(n))
        if n == int(float(n)):
            self.check_equal_hash(n, float(n))
