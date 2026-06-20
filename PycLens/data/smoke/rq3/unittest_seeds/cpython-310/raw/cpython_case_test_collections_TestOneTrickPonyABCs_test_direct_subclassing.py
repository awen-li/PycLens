# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_direct_subclassing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for B in (Hashable, Iterable, Iterator, Reversible, Sized, Container, Callable):

        class C(B):
            pass
        self.assertTrue(issubclass(C, B))
        self.assertFalse(issubclass(int, C))
