# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_cannot_instantiate_abstract

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @runtime_checkable
    class P(Protocol):

        @abc.abstractmethod
        def ameth(self) -> int:
            raise NotImplementedError

    class B(P):
        pass

    class C(B):

        def ameth(self) -> int:
            return 26
    with self.assertRaises(TypeError):
        B()
    self.assertIsInstance(C(), P)
