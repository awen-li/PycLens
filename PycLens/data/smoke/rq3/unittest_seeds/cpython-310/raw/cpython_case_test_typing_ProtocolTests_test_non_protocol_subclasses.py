# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_non_protocol_subclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class P(Protocol):
        x = 1

    @runtime_checkable
    class PR(Protocol):

        def meth(self):
            pass

    class NonP(P):
        x = 1

    class NonPR(PR):
        pass

    class C:
        x = 1

    class D:

        def meth(self):
            pass
    self.assertNotIsInstance(C(), NonP)
    self.assertNotIsInstance(D(), NonPR)
    self.assertNotIsSubclass(C, NonP)
    self.assertNotIsSubclass(D, NonPR)
    self.assertIsInstance(NonPR(), PR)
    self.assertIsSubclass(NonPR, PR)
