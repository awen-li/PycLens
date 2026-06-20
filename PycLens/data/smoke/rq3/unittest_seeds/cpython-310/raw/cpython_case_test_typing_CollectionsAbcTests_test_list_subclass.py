# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_list_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyList(typing.List[int]):
        pass
    a = MyList()
    self.assertIsInstance(a, MyList)
    self.assertIsInstance(a, typing.Sequence)
    self.assertIsSubclass(MyList, list)
    self.assertNotIsSubclass(list, MyList)
