# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_counter_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(type(typing.Counter()), collections.Counter)
    self.assertIs(type(typing.Counter[T]()), collections.Counter)
    self.assertIs(type(typing.Counter[int]()), collections.Counter)

    class C(typing.Counter[T]):
        ...
    self.assertIs(type(C[int]()), C)
