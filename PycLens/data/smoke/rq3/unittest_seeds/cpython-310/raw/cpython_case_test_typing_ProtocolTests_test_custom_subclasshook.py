# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_custom_subclasshook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class P(Protocol):
        x = 1

    class OKClass:
        pass

    class BadClass:
        x = 1

    class C(P):

        @classmethod
        def __subclasshook__(cls, other):
            return other.__name__.startswith('OK')
    self.assertIsInstance(OKClass(), C)
    self.assertNotIsInstance(BadClass(), C)
    self.assertIsSubclass(OKClass, C)
    self.assertNotIsSubclass(BadClass, C)
