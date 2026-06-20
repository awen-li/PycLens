# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(repr(range(1)), 'range(0, 1)')
    eq(repr(range(1, 2)), 'range(1, 2)')
    eq(repr(range(1, 4, 3)), 'range(1, 4, 3)')
