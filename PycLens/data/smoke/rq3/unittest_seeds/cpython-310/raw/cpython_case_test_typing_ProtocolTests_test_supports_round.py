# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_supports_round

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    issubclass(float, typing.SupportsRound)
    self.assertIsSubclass(float, typing.SupportsRound)
    self.assertIsSubclass(int, typing.SupportsRound)
    self.assertNotIsSubclass(str, typing.SupportsRound)
