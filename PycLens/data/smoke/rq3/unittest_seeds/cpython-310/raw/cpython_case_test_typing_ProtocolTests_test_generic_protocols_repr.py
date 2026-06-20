# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_generic_protocols_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    S = TypeVar('S')

    class P(Protocol[T, S]):
        pass
    self.assertTrue(repr(P[T, S]).endswith('P[~T, ~S]'))
    self.assertTrue(repr(P[int, str]).endswith('P[int, str]'))
