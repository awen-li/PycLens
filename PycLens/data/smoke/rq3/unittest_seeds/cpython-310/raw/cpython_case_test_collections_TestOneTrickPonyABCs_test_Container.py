# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Container

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    non_samples = [None, 42, 3.14, 1j, _test_gen(), (x for x in [])]
    for x in non_samples:
        self.assertNotIsInstance(x, Container)
        self.assertFalse(issubclass(type(x), Container), repr(type(x)))
    samples = [bytes(), str(), tuple(), list(), set(), frozenset(), dict(), dict().keys(), dict().items()]
    for x in samples:
        self.assertIsInstance(x, Container)
        self.assertTrue(issubclass(type(x), Container), repr(type(x)))
    self.validate_abstract_methods(Container, '__contains__')
    self.validate_isinstance(Container, '__contains__')
