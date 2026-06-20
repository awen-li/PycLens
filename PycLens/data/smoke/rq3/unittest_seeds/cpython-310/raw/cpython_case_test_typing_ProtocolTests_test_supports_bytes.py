# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_supports_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class B:

        def __bytes__(self):
            return b''
    self.assertIsSubclass(B, typing.SupportsBytes)
    self.assertNotIsSubclass(str, typing.SupportsBytes)
