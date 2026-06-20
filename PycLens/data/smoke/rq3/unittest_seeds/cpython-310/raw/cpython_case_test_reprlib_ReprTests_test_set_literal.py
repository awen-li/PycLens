# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_set_literal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(r({1}), '{1}')
    eq(r({1, 2, 3}), '{1, 2, 3}')
    eq(r({1, 2, 3, 4, 5, 6}), '{1, 2, 3, 4, 5, 6}')
    eq(r({1, 2, 3, 4, 5, 6, 7}), '{1, 2, 3, 4, 5, 6, ...}')
