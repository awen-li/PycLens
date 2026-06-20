# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_generic_protocols_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    S = TypeVar('S')

    class P(Protocol[T, S]):
        pass
    self.assertEqual(P, P)
    self.assertEqual(P[int, T], P[int, T])
    self.assertEqual(P[T, T][Tuple[T, S]][int, str], P[Tuple[int, str], Tuple[int, str]])
