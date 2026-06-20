# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_type_erasure_special

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    self.clear_caches()

    class MyTup(Tuple[T, T]):
        ...
    self.assertIs(MyTup[int]().__class__, MyTup)
    self.assertEqual(MyTup[int]().__orig_class__, MyTup[int])

    class MyDict(typing.Dict[T, T]):
        ...
    self.assertIs(MyDict[int]().__class__, MyDict)
    self.assertEqual(MyDict[int]().__orig_class__, MyDict[int])

    class MyDef(typing.DefaultDict[str, T]):
        ...
    self.assertIs(MyDef[int]().__class__, MyDef)
    self.assertEqual(MyDef[int]().__orig_class__, MyDef[int])
    if sys.version_info >= (3, 3):

        class MyChain(typing.ChainMap[str, T]):
            ...
        self.assertIs(MyChain[int]().__class__, MyChain)
        self.assertEqual(MyChain[int]().__orig_class__, MyChain[int])
