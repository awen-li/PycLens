# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_subclassing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MMA(typing.MutableMapping):
        pass
    with self.assertRaises(TypeError):
        MMA()

    class MMC(MMA):

        def __getitem__(self, k):
            return None

        def __setitem__(self, k, v):
            pass

        def __delitem__(self, k):
            pass

        def __iter__(self):
            return iter(())

        def __len__(self):
            return 0
    self.assertEqual(len(MMC()), 0)
    assert callable(MMC.update)
    self.assertIsInstance(MMC(), typing.Mapping)

    class MMB(typing.MutableMapping[KT, VT]):

        def __getitem__(self, k):
            return None

        def __setitem__(self, k, v):
            pass

        def __delitem__(self, k):
            pass

        def __iter__(self):
            return iter(())

        def __len__(self):
            return 0
    self.assertEqual(len(MMB()), 0)
    self.assertEqual(len(MMB[str, str]()), 0)
    self.assertEqual(len(MMB[KT, VT]()), 0)
    self.assertNotIsSubclass(dict, MMA)
    self.assertNotIsSubclass(dict, MMB)
    self.assertIsSubclass(MMA, typing.Mapping)
    self.assertIsSubclass(MMB, typing.Mapping)
    self.assertIsSubclass(MMC, typing.Mapping)
    self.assertIsInstance(MMB[KT, VT](), typing.Mapping)
    self.assertIsInstance(MMB[KT, VT](), collections.abc.Mapping)
    self.assertIsSubclass(MMA, collections.abc.Mapping)
    self.assertIsSubclass(MMB, collections.abc.Mapping)
    self.assertIsSubclass(MMC, collections.abc.Mapping)
    with self.assertRaises(TypeError):
        issubclass(MMB[str, str], typing.Mapping)
    self.assertIsSubclass(MMC, MMA)

    class I(typing.Iterable):
        ...
    self.assertNotIsSubclass(list, I)

    class G(typing.Generator[int, int, int]):
        ...

    def g():
        yield 0
    self.assertIsSubclass(G, typing.Generator)
    self.assertIsSubclass(G, typing.Iterable)
    self.assertIsSubclass(G, collections.abc.Generator)
    self.assertIsSubclass(G, collections.abc.Iterable)
    self.assertNotIsSubclass(type(g), G)
