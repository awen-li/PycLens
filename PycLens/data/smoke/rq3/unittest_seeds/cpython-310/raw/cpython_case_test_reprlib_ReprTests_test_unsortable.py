# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_unsortable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = set([1j, 2j, 3j])
    y = frozenset(x)
    z = {1j: 1, 2j: 2}
    r(x)
    r(y)
    r(z)
