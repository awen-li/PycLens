# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_defaultdict_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyDefDict(typing.DefaultDict[str, int]):
        pass
    dd = MyDefDict()
    self.assertIsInstance(dd, MyDefDict)
    self.assertIsSubclass(MyDefDict, collections.defaultdict)
    self.assertNotIsSubclass(collections.defaultdict, MyDefDict)
