# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Hashable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    non_samples = [bytearray(), list(), set(), dict()]
    for x in non_samples:
        self.assertNotIsInstance(x, Hashable)
        self.assertFalse(issubclass(type(x), Hashable), repr(type(x)))
    samples = [None, int(), float(), complex(), str(), tuple(), frozenset(), int, list, object, type, bytes()]
    for x in samples:
        self.assertIsInstance(x, Hashable)
        self.assertTrue(issubclass(type(x), Hashable), repr(type(x)))
    self.assertRaises(TypeError, Hashable)

    class H(Hashable):

        def __hash__(self):
            return super().__hash__()
    self.assertEqual(hash(H()), 0)
    self.assertFalse(issubclass(int, H))
    self.validate_abstract_methods(Hashable, '__hash__')
    self.validate_isinstance(Hashable, '__hash__')
