# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Sized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    non_samples = [None, 42, 3.14, 1j, _test_gen(), (x for x in [])]
    for x in non_samples:
        self.assertNotIsInstance(x, Sized)
        self.assertFalse(issubclass(type(x), Sized), repr(type(x)))
    samples = [bytes(), str(), tuple(), list(), set(), frozenset(), dict(), dict().keys(), dict().items(), dict().values()]
    for x in samples:
        self.assertIsInstance(x, Sized)
        self.assertTrue(issubclass(type(x), Sized), repr(type(x)))
    self.validate_abstract_methods(Sized, '__len__')
    self.validate_isinstance(Sized, '__len__')
