# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_ordereddict_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(type(typing.OrderedDict()), collections.OrderedDict)
    self.assertIs(type(typing.OrderedDict[KT, VT]()), collections.OrderedDict)
    self.assertIs(type(typing.OrderedDict[str, int]()), collections.OrderedDict)
