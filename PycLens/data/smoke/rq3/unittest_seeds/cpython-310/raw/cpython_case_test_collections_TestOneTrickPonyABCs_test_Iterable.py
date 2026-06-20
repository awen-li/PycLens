# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Iterable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    non_samples = [None, 42, 3.14, 1j]
    for x in non_samples:
        self.assertNotIsInstance(x, Iterable)
        self.assertFalse(issubclass(type(x), Iterable), repr(type(x)))
    samples = [bytes(), str(), tuple(), list(), set(), frozenset(), dict(), dict().keys(), dict().items(), dict().values(), _test_gen(), (x for x in [])]
    for x in samples:
        self.assertIsInstance(x, Iterable)
        self.assertTrue(issubclass(type(x), Iterable), repr(type(x)))

    class I(Iterable):

        def __iter__(self):
            return super().__iter__()
    self.assertEqual(list(I()), [])
    self.assertFalse(issubclass(str, I))
    self.validate_abstract_methods(Iterable, '__iter__')
    self.validate_isinstance(Iterable, '__iter__')

    class It:

        def __iter__(self):
            return iter([])

    class ItBlocked(It):
        __iter__ = None
    self.assertTrue(issubclass(It, Iterable))
    self.assertTrue(isinstance(It(), Iterable))
    self.assertFalse(issubclass(ItBlocked, Iterable))
    self.assertFalse(isinstance(ItBlocked(), Iterable))
