# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_non_runtime_protocol_isinstance_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class P(Protocol):
        x: int
    with self.assertRaisesRegex(TypeError, '@runtime_checkable'):
        isinstance(1, P)
