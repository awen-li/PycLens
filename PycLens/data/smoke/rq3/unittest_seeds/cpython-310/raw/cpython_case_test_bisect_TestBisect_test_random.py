# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestBisect_test_random

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from random import randrange
    for i in range(n):
        data = [randrange(0, n, 2) for j in range(i)]
        data.sort()
        elem = randrange(-1, n + 1)
        ip = self.module.bisect_left(data, elem)
        if ip < len(data):
            self.assertTrue(elem <= data[ip])
        if ip > 0:
            self.assertTrue(data[ip - 1] < elem)
        ip = self.module.bisect_right(data, elem)
        if ip < len(data):
            self.assertTrue(elem < data[ip])
        if ip > 0:
            self.assertTrue(data[ip - 1] <= elem)
