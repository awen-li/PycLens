# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_supports_abs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsSubclass(float, typing.SupportsAbs)
    self.assertIsSubclass(int, typing.SupportsAbs)
    self.assertNotIsSubclass(str, typing.SupportsAbs)
