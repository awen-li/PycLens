# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_none_treated_correctly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @runtime_checkable
    class P(Protocol):
        x = None

    class B(object):
        pass
    self.assertNotIsInstance(B(), P)

    class C:
        x = 1

    class D:
        x = None
    self.assertIsInstance(C(), P)
    self.assertIsInstance(D(), P)

    class CI:

        def __init__(self):
            self.x = 1

    class DI:

        def __init__(self):
            self.x = None
    self.assertIsInstance(CI(), P)
    self.assertIsInstance(DI(), P)
