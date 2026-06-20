# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_collections_as_base

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M(collections.abc.Mapping):
        ...
    self.assertIsSubclass(M, typing.Mapping)
    self.assertIsSubclass(M, typing.Iterable)

    class S(collections.abc.MutableSequence):
        ...
    self.assertIsSubclass(S, typing.MutableSequence)
    self.assertIsSubclass(S, typing.Iterable)

    class I(collections.abc.Iterable):
        ...
    self.assertIsSubclass(I, typing.Iterable)

    class A(collections.abc.Mapping, metaclass=abc.ABCMeta):
        ...

    class B:
        ...
    A.register(B)
    self.assertIsSubclass(B, typing.Mapping)
