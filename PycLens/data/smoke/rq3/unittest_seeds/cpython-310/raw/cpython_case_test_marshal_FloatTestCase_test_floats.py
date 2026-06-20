# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: FloatTestCase_test_floats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    small = 1e-25
    n = sys.maxsize * 3.7e+250
    while n > small:
        for expected in (-n, n):
            self.helper(float(expected))
        n /= 123.4567
    f = 0.0
    s = marshal.dumps(f, 2)
    got = marshal.loads(s)
    self.assertEqual(f, got)
    s = marshal.dumps(f, 1)
    got = marshal.loads(s)
    self.assertEqual(f, got)
    n = sys.maxsize * 3.7e-250
    while n < small:
        for expected in (-n, n):
            f = float(expected)
            self.helper(f)
            self.helper(f, 1)
        n *= 123.4567
