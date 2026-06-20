# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_numbers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(r(123), repr(123))
    eq(r(123), repr(123))
    eq(r(1.0 / 3), repr(1.0 / 3))
    n = 10 ** 100
    expected = repr(n)[:18] + '...' + repr(n)[-19:]
    eq(r(n), expected)
