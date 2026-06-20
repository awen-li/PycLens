# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_no_inheritance_from_nominal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        pass

    class BP(Protocol):
        pass
    with self.assertRaises(TypeError):

        class P(C, Protocol):
            pass
    with self.assertRaises(TypeError):

        class P(Protocol, C):
            pass
    with self.assertRaises(TypeError):

        class P(BP, C, Protocol):
            pass

    class D(BP, C):
        pass

    class E(C, BP):
        pass
    self.assertNotIsInstance(D(), E)
    self.assertNotIsInstance(E(), D)
