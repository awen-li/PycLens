# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(r((1,)), '(1,)')
    t3 = (1, 2, 3)
    eq(r(t3), '(1, 2, 3)')
    r2 = Repr()
    r2.maxtuple = 2
    expected = repr(t3)[:-2] + '...)'
    eq(r2.repr(t3), expected)
