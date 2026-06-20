# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_isinstance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    @runtime_checkable
    class P(Protocol):

        def meth(x):
            ...

    @runtime_checkable
    class PG(Protocol[T]):

        def meth(x):
            ...

    class BadP(Protocol):

        def meth(x):
            ...

    class BadPG(Protocol[T]):

        def meth(x):
            ...

    class C:

        def meth(x):
            ...
    self.assertIsInstance(C(), P)
    self.assertIsInstance(C(), PG)
    with self.assertRaises(TypeError):
        isinstance(C(), PG[T])
    with self.assertRaises(TypeError):
        isinstance(C(), PG[C])
    with self.assertRaises(TypeError):
        isinstance(C(), BadP)
    with self.assertRaises(TypeError):
        isinstance(C(), BadPG)
