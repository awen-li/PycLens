# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Reversible

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    non_samples = [None, 42, 3.14, 1j, set(), frozenset()]
    for x in non_samples:
        self.assertNotIsInstance(x, Reversible)
        self.assertFalse(issubclass(type(x), Reversible), repr(type(x)))
    non_reversibles = [_test_gen(), (x for x in []), iter([]), reversed([])]
    for x in non_reversibles:
        self.assertNotIsInstance(x, Reversible)
        self.assertFalse(issubclass(type(x), Reversible), repr(type(x)))
    samples = [bytes(), str(), tuple(), list(), OrderedDict(), OrderedDict().keys(), OrderedDict().items(), OrderedDict().values(), Counter(), Counter().keys(), Counter().items(), Counter().values(), dict(), dict().keys(), dict().items(), dict().values()]
    for x in samples:
        self.assertIsInstance(x, Reversible)
        self.assertTrue(issubclass(type(x), Reversible), repr(type(x)))
    self.assertTrue(issubclass(Sequence, Reversible), repr(Sequence))
    self.assertFalse(issubclass(Mapping, Reversible), repr(Mapping))
    self.assertFalse(issubclass(MutableMapping, Reversible), repr(MutableMapping))

    class R(Reversible):

        def __iter__(self):
            return iter(list())

        def __reversed__(self):
            return iter(list())
    self.assertEqual(list(reversed(R())), [])
    self.assertFalse(issubclass(float, R))
    self.validate_abstract_methods(Reversible, '__reversed__', '__iter__')

    class RevNoIter:

        def __reversed__(self):
            return reversed([])

    class RevPlusIter(RevNoIter):

        def __iter__(self):
            return iter([])
    self.assertFalse(issubclass(RevNoIter, Reversible))
    self.assertFalse(isinstance(RevNoIter(), Reversible))
    self.assertTrue(issubclass(RevPlusIter, Reversible))
    self.assertTrue(isinstance(RevPlusIter(), Reversible))

    class Rev:

        def __iter__(self):
            return iter([])

        def __reversed__(self):
            return reversed([])

    class RevItBlocked(Rev):
        __iter__ = None

    class RevRevBlocked(Rev):
        __reversed__ = None
    self.assertTrue(issubclass(Rev, Reversible))
    self.assertTrue(isinstance(Rev(), Reversible))
    self.assertFalse(issubclass(RevItBlocked, Reversible))
    self.assertFalse(isinstance(RevItBlocked(), Reversible))
    self.assertFalse(issubclass(RevRevBlocked, Reversible))
    self.assertFalse(isinstance(RevRevBlocked(), Reversible))
