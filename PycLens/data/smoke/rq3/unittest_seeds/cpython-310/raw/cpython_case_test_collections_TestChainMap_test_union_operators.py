# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestChainMap_test_union_operators

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cm1 = ChainMap(dict(a=1, b=2), dict(c=3, d=4))
    cm2 = ChainMap(dict(a=10, e=5), dict(b=20, d=4))
    cm3 = cm1.copy()
    d = dict(a=10, c=30)
    pairs = [('c', 3), ('p', 0)]
    tmp = cm1 | cm2
    self.assertEqual(tmp.maps, [cm1.maps[0] | dict(cm2), *cm1.maps[1:]])
    cm1 |= cm2
    self.assertEqual(tmp, cm1)
    tmp = cm2 | d
    self.assertEqual(tmp.maps, [cm2.maps[0] | d, *cm2.maps[1:]])
    self.assertEqual((d | cm2).maps, [d | dict(cm2)])
    cm2 |= d
    self.assertEqual(tmp, cm2)
    with self.assertRaises(TypeError):
        cm3 | pairs
    tmp = cm3.copy()
    cm3 |= pairs
    self.assertEqual(cm3.maps, [tmp.maps[0] | dict(pairs), *tmp.maps[1:]])

    class Subclass(ChainMap):
        pass

    class SubclassRor(ChainMap):

        def __ror__(self, other):
            return super().__ror__(other)
    tmp = ChainMap() | ChainMap()
    self.assertIs(type(tmp), ChainMap)
    self.assertIs(type(tmp.maps[0]), dict)
    tmp = ChainMap() | Subclass()
    self.assertIs(type(tmp), ChainMap)
    self.assertIs(type(tmp.maps[0]), dict)
    tmp = Subclass() | ChainMap()
    self.assertIs(type(tmp), Subclass)
    self.assertIs(type(tmp.maps[0]), dict)
    tmp = ChainMap() | SubclassRor()
    self.assertIs(type(tmp), SubclassRor)
    self.assertIs(type(tmp.maps[0]), dict)
