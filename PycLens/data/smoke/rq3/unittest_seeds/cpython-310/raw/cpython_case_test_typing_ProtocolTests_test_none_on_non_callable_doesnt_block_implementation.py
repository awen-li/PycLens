# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_none_on_non_callable_doesnt_block_implementation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @runtime_checkable
    class P(Protocol):
        x = 1

    class A:
        x = 1

    class B(A):
        x = None

    class C:

        def __init__(self):
            self.x = None
    self.assertIsInstance(B(), P)
    self.assertIsInstance(C(), P)
