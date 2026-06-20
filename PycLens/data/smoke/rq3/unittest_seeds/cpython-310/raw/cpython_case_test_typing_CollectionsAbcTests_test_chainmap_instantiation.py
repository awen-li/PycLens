# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_chainmap_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(type(typing.ChainMap()), collections.ChainMap)
    self.assertIs(type(typing.ChainMap[KT, VT]()), collections.ChainMap)
    self.assertIs(type(typing.ChainMap[str, int]()), collections.ChainMap)

    class CM(typing.ChainMap[KT, VT]):
        ...
    self.assertIs(type(CM[int, str]()), CM)
