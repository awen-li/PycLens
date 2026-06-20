# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: IntTestCase_test_ints

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = sys.maxsize ** 2
    while n:
        for expected in (-n, n):
            self.helper(expected)
        n = n >> 1
