# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_basic_protocol

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @runtime_checkable
    class P(Protocol):

        def meth(self):
            pass

    class C:
        pass

    class D:

        def meth(self):
            pass

    def f():
        pass
    self.assertIsSubclass(D, P)
    self.assertIsInstance(D(), P)
    self.assertNotIsSubclass(C, P)
    self.assertNotIsInstance(C(), P)
    self.assertNotIsSubclass(types.FunctionType, P)
    self.assertNotIsInstance(f, P)
