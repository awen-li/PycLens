# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_abc_registry_kept

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class C(collections.abc.Mapping, Generic[T]):
        ...
    C.register(int)
    self.assertIsInstance(1, C)
    C[int]
    self.assertIsInstance(1, C)
    C._abc_registry_clear()
    C._abc_caches_clear()
