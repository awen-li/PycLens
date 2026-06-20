# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocol_checks_after_subscript

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class P(Protocol[T]):
        pass

    class C(P[T]):
        pass

    class Other1:
        pass

    class Other2:
        pass
    CA = C[Any]
    self.assertNotIsInstance(Other1(), C)
    self.assertNotIsSubclass(Other2, C)

    class D1(C[Any]):
        pass

    class D2(C[Any]):
        pass
    CI = C[int]
    self.assertIsInstance(D1(), C)
    self.assertIsSubclass(D2, C)
