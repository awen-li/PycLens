# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_bad_subscripts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    S = TypeVar('S')
    with self.assertRaises(TypeError):

        class P(Protocol[T, T]):
            pass
    with self.assertRaises(TypeError):

        class P(Protocol[int]):
            pass
    with self.assertRaises(TypeError):

        class P(Protocol[T], Protocol[S]):
            pass
    with self.assertRaises(TypeError):

        class P(typing.Mapping[T, S], Protocol[T]):
            pass
