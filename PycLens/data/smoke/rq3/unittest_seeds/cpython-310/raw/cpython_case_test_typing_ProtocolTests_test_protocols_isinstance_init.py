# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_isinstance_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    @runtime_checkable
    class P(Protocol):
        x = 1

    @runtime_checkable
    class PG(Protocol[T]):
        x = 1

    class C:

        def __init__(self, x):
            self.x = x
    self.assertIsInstance(C(1), P)
    self.assertIsInstance(C(1), PG)
