# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = namedtuple('A', 'x')
    self.assertEqual(repr(A(1)), 'A(x=1)')

    class B(A):
        pass
    self.assertEqual(repr(B(1)), 'B(x=1)')
