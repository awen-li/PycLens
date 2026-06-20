# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_supports_complex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __complex__(self):
            return 0j
    self.assertIsSubclass(C, typing.SupportsComplex)
    self.assertNotIsSubclass(str, typing.SupportsComplex)
