# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_issubclass_non_callable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        x = 1

    @runtime_checkable
    class PNonCall(Protocol):
        x = 1
    with self.assertRaises(TypeError):
        issubclass(C, PNonCall)
    self.assertIsInstance(C(), PNonCall)
    PNonCall.register(C)
    with self.assertRaises(TypeError):
        issubclass(C, PNonCall)
    self.assertIsInstance(C(), PNonCall)

    class D(PNonCall):
        ...
    self.assertNotIsSubclass(C, D)
    self.assertNotIsInstance(C(), D)
    D.register(C)
    self.assertIsSubclass(C, D)
    self.assertIsInstance(C(), D)
    with self.assertRaises(TypeError):
        issubclass(D, PNonCall)
