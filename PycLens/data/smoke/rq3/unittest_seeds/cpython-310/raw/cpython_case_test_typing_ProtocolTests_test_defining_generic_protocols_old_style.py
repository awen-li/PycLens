# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_defining_generic_protocols_old_style

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    S = TypeVar('S')

    @runtime_checkable
    class PR(Protocol, Generic[T, S]):

        def meth(self):
            pass

    class P(PR[int, str], Protocol):
        y = 1
    with self.assertRaises(TypeError):
        issubclass(PR[int, str], PR)
    self.assertIsSubclass(P, PR)
    with self.assertRaises(TypeError):
        PR[int]

    class P1(Protocol, Generic[T]):

        def bar(self, x: T) -> str:
            ...

    class P2(Generic[T], Protocol):

        def bar(self, x: T) -> str:
            ...

    @runtime_checkable
    class PSub(P1[str], Protocol):
        x = 1

    class Test:
        x = 1

        def bar(self, x: str) -> str:
            return x
    self.assertIsInstance(Test(), PSub)
