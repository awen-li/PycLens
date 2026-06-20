# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_deque_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(type(typing.Deque()), collections.deque)
    self.assertIs(type(typing.Deque[T]()), collections.deque)
    self.assertIs(type(typing.Deque[int]()), collections.deque)

    class D(typing.Deque[T]):
        ...
    self.assertIs(type(D[int]()), D)
