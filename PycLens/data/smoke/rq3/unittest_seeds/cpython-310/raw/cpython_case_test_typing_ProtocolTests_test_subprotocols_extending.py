# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_subprotocols_extending

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class P1(Protocol):

        def meth1(self):
            pass

    @runtime_checkable
    class P2(P1, Protocol):

        def meth2(self):
            pass

    class C:

        def meth1(self):
            pass

        def meth2(self):
            pass

    class C1:

        def meth1(self):
            pass

    class C2:

        def meth2(self):
            pass
    self.assertNotIsInstance(C1(), P2)
    self.assertNotIsInstance(C2(), P2)
    self.assertNotIsSubclass(C1, P2)
    self.assertNotIsSubclass(C2, P2)
    self.assertIsInstance(C(), P2)
    self.assertIsSubclass(C, P2)
