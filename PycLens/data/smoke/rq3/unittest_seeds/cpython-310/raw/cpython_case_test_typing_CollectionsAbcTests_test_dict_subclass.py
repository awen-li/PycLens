# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_dict_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyDict(typing.Dict[str, int]):
        pass
    d = MyDict()
    self.assertIsInstance(d, MyDict)
    self.assertIsInstance(d, typing.MutableMapping)
    self.assertIsSubclass(MyDict, dict)
    self.assertNotIsSubclass(dict, MyDict)
