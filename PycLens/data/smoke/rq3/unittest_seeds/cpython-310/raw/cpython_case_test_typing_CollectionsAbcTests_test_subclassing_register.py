# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_subclassing_register

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(typing.Container):
        ...

    class B(A):
        ...

    class C:
        ...
    A.register(C)
    self.assertIsSubclass(C, A)
    self.assertNotIsSubclass(C, B)

    class D:
        ...
    B.register(D)
    self.assertIsSubclass(D, A)
    self.assertIsSubclass(D, B)

    class M:
        ...
    collections.abc.MutableMapping.register(M)
    self.assertIsSubclass(M, typing.Mapping)
