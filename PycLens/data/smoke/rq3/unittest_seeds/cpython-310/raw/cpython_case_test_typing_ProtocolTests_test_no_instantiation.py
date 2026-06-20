# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_no_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class P(Protocol):
        pass
    with self.assertRaises(TypeError):
        P()

    class C(P):
        pass
    self.assertIsInstance(C(), C)
    with self.assertRaises(TypeError):
        C(42)
    T = TypeVar('T')

    class PG(Protocol[T]):
        pass
    with self.assertRaises(TypeError):
        PG()
    with self.assertRaises(TypeError):
        PG[int]()
    with self.assertRaises(TypeError):
        PG[T]()

    class CG(PG[T]):
        pass
    self.assertIsInstance(CG[int](), CG)
    with self.assertRaises(TypeError):
        CG[int](42)
