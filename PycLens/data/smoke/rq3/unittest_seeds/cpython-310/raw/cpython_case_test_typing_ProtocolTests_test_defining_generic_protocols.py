# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_defining_generic_protocols

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    S = TypeVar('S')

    @runtime_checkable
    class PR(Protocol[T, S]):

        def meth(self):
            pass

    class P(PR[int, T], Protocol[T]):
        y = 1
    with self.assertRaises(TypeError):
        PR[int]
    with self.assertRaises(TypeError):
        P[int, str]

    class C(PR[int, T]):
        pass
    self.assertIsInstance(C[str](), C)
