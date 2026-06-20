# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_issubclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    @runtime_checkable
    class P(Protocol):

        def x(self):
            ...

    @runtime_checkable
    class PG(Protocol[T]):

        def x(self):
            ...

    class BadP(Protocol):

        def x(self):
            ...

    class BadPG(Protocol[T]):

        def x(self):
            ...

    class C:

        def x(self):
            ...
    self.assertIsSubclass(C, P)
    self.assertIsSubclass(C, PG)
    self.assertIsSubclass(BadP, PG)
    with self.assertRaises(TypeError):
        issubclass(C, PG[T])
    with self.assertRaises(TypeError):
        issubclass(C, PG[C])
    with self.assertRaises(TypeError):
        issubclass(C, BadP)
    with self.assertRaises(TypeError):
        issubclass(C, BadPG)
    with self.assertRaises(TypeError):
        issubclass(P, PG[T])
    with self.assertRaises(TypeError):
        issubclass(PG, PG[int])
