# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_registration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for B in (Hashable, Iterable, Iterator, Reversible, Sized, Container, Callable):

        class C:
            __hash__ = None
        self.assertFalse(issubclass(C, B), B.__name__)
        B.register(C)
        self.assertTrue(issubclass(C, B))
