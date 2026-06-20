# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_chainmap_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyChainMap(typing.ChainMap[str, int]):
        pass
    cm = MyChainMap()
    self.assertIsInstance(cm, MyChainMap)
    self.assertIsSubclass(MyChainMap, collections.ChainMap)
    self.assertNotIsSubclass(collections.ChainMap, MyChainMap)
