# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Collection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    non_collections = [None, 42, 3.14, 1j, lambda x: 2 * x]
    for x in non_collections:
        self.assertNotIsInstance(x, Collection)
        self.assertFalse(issubclass(type(x), Collection), repr(type(x)))
    non_col_iterables = [_test_gen(), iter(b''), iter(bytearray()), (x for x in [])]
    for x in non_col_iterables:
        self.assertNotIsInstance(x, Collection)
        self.assertFalse(issubclass(type(x), Collection), repr(type(x)))
    samples = [set(), frozenset(), dict(), bytes(), str(), tuple(), list(), dict().keys(), dict().items(), dict().values()]
    for x in samples:
        self.assertIsInstance(x, Collection)
        self.assertTrue(issubclass(type(x), Collection), repr(type(x)))
    self.assertTrue(issubclass(Sequence, Collection), repr(Sequence))
    self.assertTrue(issubclass(Mapping, Collection), repr(Mapping))
    self.assertTrue(issubclass(MutableMapping, Collection), repr(MutableMapping))
    self.assertTrue(issubclass(Set, Collection), repr(Set))
    self.assertTrue(issubclass(MutableSet, Collection), repr(MutableSet))
    self.assertTrue(issubclass(Sequence, Collection), repr(MutableSet))

    class Col(Collection):

        def __iter__(self):
            return iter(list())

        def __len__(self):
            return 0

        def __contains__(self, item):
            return False

    class DerCol(Col):
        pass
    self.assertEqual(list(iter(Col())), [])
    self.assertFalse(issubclass(list, Col))
    self.assertFalse(issubclass(set, Col))
    self.assertFalse(issubclass(float, Col))
    self.assertEqual(list(iter(DerCol())), [])
    self.assertFalse(issubclass(list, DerCol))
    self.assertFalse(issubclass(set, DerCol))
    self.assertFalse(issubclass(float, DerCol))
    self.validate_abstract_methods(Collection, '__len__', '__iter__', '__contains__')

    class ColNoIter:

        def __len__(self):
            return 0

        def __contains__(self, item):
            return False

    class ColNoSize:

        def __iter__(self):
            return iter([])

        def __contains__(self, item):
            return False

    class ColNoCont:

        def __iter__(self):
            return iter([])

        def __len__(self):
            return 0
    self.assertFalse(issubclass(ColNoIter, Collection))
    self.assertFalse(isinstance(ColNoIter(), Collection))
    self.assertFalse(issubclass(ColNoSize, Collection))
    self.assertFalse(isinstance(ColNoSize(), Collection))
    self.assertFalse(issubclass(ColNoCont, Collection))
    self.assertFalse(isinstance(ColNoCont(), Collection))

    class SizeBlock:

        def __iter__(self):
            return iter([])

        def __contains__(self):
            return False
        __len__ = None

    class IterBlock:

        def __len__(self):
            return 0

        def __contains__(self):
            return True
        __iter__ = None
    self.assertFalse(issubclass(SizeBlock, Collection))
    self.assertFalse(isinstance(SizeBlock(), Collection))
    self.assertFalse(issubclass(IterBlock, Collection))
    self.assertFalse(isinstance(IterBlock(), Collection))

    class ColImpl:

        def __iter__(self):
            return iter(list())

        def __len__(self):
            return 0

        def __contains__(self, item):
            return False

    class NonCol(ColImpl):
        __contains__ = None
    self.assertFalse(issubclass(NonCol, Collection))
    self.assertFalse(isinstance(NonCol(), Collection))
