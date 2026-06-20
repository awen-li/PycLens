# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: AssortedBytesTest_test_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsNotNone(bytearray.__doc__)
    self.assertTrue(bytearray.__doc__.startswith('bytearray('), bytearray.__doc__)
    self.assertIsNotNone(bytes.__doc__)
    self.assertTrue(bytes.__doc__.startswith('bytes('), bytes.__doc__)
