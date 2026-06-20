# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_support_register

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @runtime_checkable
    class P(Protocol):
        x = 1

    class PM(Protocol):

        def meth(self):
            pass

    class D(PM):
        pass

    class C:
        pass
    D.register(C)
    P.register(C)
    self.assertIsInstance(C(), P)
    self.assertIsInstance(C(), D)
