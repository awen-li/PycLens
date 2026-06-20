# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_deque

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsSubclass(collections.deque, typing.Deque)

    class MyDeque(typing.Deque[int]):
        ...
    self.assertIsInstance(MyDeque(), collections.deque)
