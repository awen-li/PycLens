# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_ByteString

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for sample in [bytes, bytearray]:
        self.assertIsInstance(sample(), ByteString)
        self.assertTrue(issubclass(sample, ByteString))
    for sample in [str, list, tuple]:
        self.assertNotIsInstance(sample(), ByteString)
        self.assertFalse(issubclass(sample, ByteString))
    self.assertNotIsInstance(memoryview(b''), ByteString)
    self.assertFalse(issubclass(memoryview, ByteString))
    self.validate_abstract_methods(ByteString, '__getitem__', '__len__')
