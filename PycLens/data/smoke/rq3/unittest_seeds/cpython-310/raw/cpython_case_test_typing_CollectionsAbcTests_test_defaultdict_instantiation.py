# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_defaultdict_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(type(typing.DefaultDict()), collections.defaultdict)
    self.assertIs(type(typing.DefaultDict[KT, VT]()), collections.defaultdict)
    self.assertIs(type(typing.DefaultDict[str, int]()), collections.defaultdict)
